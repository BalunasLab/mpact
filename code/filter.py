"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import pandas as pd
import numpy as np
import math
import scipy.cluster.hierarchy as spc

class ionmerge: #source and target list for ions to merge for mispicked filter
    def __init__(self, target, sources):
            self.target = target
            self.sources = []
            self.sources.append(sources)

class ionfilter: #general ionfilter class with paramerters and list of ions to remove
                #may not use long term since everything is in the iondict file now
        def __init__(self, parameters, ionlist):
            self.params = parameters
            self.ions = ionlist
            self.merge = []
            

        
def reformatcorr(corr): #reformatts correlation matrix to generate a list from sequential columns
        # output list/series is used for deconvolution of ions
        #reformat to for pos in range(1:corr.shape[0]) or something like that
    corr = corr.to_numpy()
    reformatted = corr[1:,0]
    pos = 1
    while pos < corr.shape[0]:
        reformatted = np.append(reformatted, corr[pos+1:,pos], axis=0)
        pos = pos + 1
    reformatted = 1-np.where(reformatted<0, 0, reformatted)
    return(reformatted)

def decon(analysis_params, ionfilters): #in source ion filter based on correlation matrix deconvolution
            # need to save in source spectra
    msdata_ind  = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [2], index_col = [0,1]).iloc[:,:1]
    rtlist = msdata_ind['Retention time (min)'].unique()
    msdata_ind = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [2], index_col = [0]).iloc[:,:2]
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [2], index_col = [0]).iloc[:,2:]
    
    singleslist = []
    insourcelist = []
    clusterlist = []
    clusterdfs = []
    filtereddf = msdata_ind 
    ftrgrps = {}
    for elem in rtlist:
        filtereddf = msdata_ind.loc[msdata_ind.iloc[:,1] == elem, :]
        if len(filtereddf.index) == 1:
            singleslist.append(filtereddf.index.to_list()[0])
        else:
            unseplist = filtereddf.index.tolist()
            filtereddf2 = msdata.loc[unseplist, :].transpose()
            corr = filtereddf2.corr()
            corr2 = reformatcorr(corr)
            linkage = spc.linkage(corr2, method='complete')
            np.clip(linkage, 0, None, linkage)
            idx = spc.fcluster(linkage, 1-analysis_params.deconthresh, 'distance')
            
            decongroups = {}
            for group in range(1, max(idx) + 1):
                decongroups[group] = []
            for peak in range(0, idx.shape[0]):
                if (peak < len(unseplist)): #added this to get bruker data to work
                    decongroups[idx[peak]].append(unseplist[peak])
            for group in decongroups:
                if len(decongroups[group]) == 1:
                    singleslist.append(decongroups[group][0])
                else:
                    clusterlist.append(decongroups[group])
                    tempdf = msdata_ind.loc[decongroups[group]].sort_values(by=['m/z'], ascending=False)
                    #tempdf['neutral'] = tempdf['m/z'] - 1.007825 This code would start to figure out if something is an oligomer, gonna wait on this for a bit tho
                    #tempdf['type'] = 'fragment'
                    if len(tempdf.index.to_list()) > 0: #added this to get bruker data to work
                        singleslist.append(tempdf.index.to_list()[0])
                        insourcelist += tempdf.index.to_list()[1:]
                        clusterdfs.append(tempdf)
                    
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [0,1,2], index_col = [0])
    msdata = msdata.loc[singleslist]
    msdata.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), header = True, index = True)
    ionfilters['insource'] = ionfilter('', insourcelist)
    
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = 0) #block adds average and median cv to iondict.csv
    iondict['pass_insource'] = ~iondict.index.isin(ionfilters['insource'].ions)
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header = True, index = True)

    return(ionfilters)

# -----CV Filtering-----
def listfilter(msdata, ionlist, include):
    if include == True:
        msdata = msdata[msdata.iloc[:, 0].isin(ionlist)]
    else:
        msdata = msdata[~msdata.iloc[:, 0].isin(ionlist)]
    return(msdata)

def groupfilter(group, msdata_blankfilterg, analysis_params): #filter ions over abundance threshold in list. Would be better to use a relative rather than absolute threshold
    msdata_blankfilterg = msdata_blankfilterg[msdata_blankfilterg[group] > analysis_params.blankfilthresh] # filters ions based on group presence > 100 ions/abundance
    msdata_blankfilterg = msdata_blankfilterg.reset_index()
    groupfilterlist = msdata_blankfilterg.iloc[0:,0].tolist() #returns filtered df index as list
    return groupfilterlist

def parsionlists(analysis_params): #parses lists of ions present in each group
    msdata_blankfilterg = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_groupaverages.csv'), sep = ',', header = [0], index_col = [0, 1, 2, 3]).unstack()
    msdata_blankfilterg.columns = msdata_blankfilterg.columns.droplevel()
    msdata_blankfilterg['max']=msdata_blankfilterg.max(numeric_only = True, axis = 1)
    for column in msdata_blankfilterg:
        msdata_blankfilterg[column] = msdata_blankfilterg[column]/msdata_blankfilterg['max']
    msdata_blankfilterg = msdata_blankfilterg.drop(columns=['max'])
    biolgroups = msdata_blankfilterg.columns.tolist()
    groupionlists={}
    for group in biolgroups:
        groupionlists[group] = groupfilter(group, msdata_blankfilterg, analysis_params)   
    return(groupionlists)

def cvfilter(analysis_params, ionfilterlist, threshold): #cv filter code NEED TO REMOVE MSDATAINPUT NOT NEEDED NOW

    print('Running CV filter')
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [0, 1, 2], index_col = [0, 1, 2]) #imports data
    msdata = msdata.stack([0,1,2])
    msdata = (msdata.groupby(level = [0,1,2,3,4]).std() / msdata.groupby(level = [0,1,2,3,4]).mean())
    msdatameancv = msdata.groupby(level = 0).mean().to_frame()
    msdatamediancv = msdata.groupby(level = 0).median().to_frame()
    
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = 0) #block adds average and median cv to iondict.csv
    iondict['average CV'] = msdatameancv.iloc[:,0]
    iondict['median CV'] = msdatamediancv.iloc[:,0]
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header = True, index = True)

    
    #following format of getting ions to keep and then finding ions to reject is done to make sure ions with NaN values are excluded
    msdata_filtered = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [0, 1, 2], index_col = [0]) # added this to get peak list right before cv 
                    #filtering now that blankfiltering and peak corr is baked in
    ionlist = msdata_filtered.index.tolist() # list of all ions
    iondict = iondict[iondict[analysis_params.cvparam] < threshold] 
    cvkeeplist = iondict.index.tolist() # list of ions to keep
    cvfilterlist = list(set(ionlist) - set(cvkeeplist)) # list of ions to reject
    ionfilterlist['cv'] = ionfilter(analysis_params.cvthresh, cvfilterlist)
    
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = 0)
    iondict['pass_cvfil'] = ~iondict.index.isin(ionfilterlist['cv'].ions)
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header = True, index = True) #saves formatted backup for later use
    return(ionfilterlist)

# -----Deringing and relational filter algorithm-----
def relationalfilter(analysis_params, ionfilterlist):#clean up index formatting, pull from ionmetadata
                                                    #will need to change how this function is called when merging before other analysis is desired
    #initial processing for ringing filter. Imports data, sorts by m/z, and converts to numpy array
    print('Running relational filter')
    pdindex = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [2], index_col = None)
    pdindex.drop(pdindex.columns.difference(['Compound','m/z','Retention time (min)']), 1, inplace=True)
    pdindex = pdindex.sort_values(['m/z'], ascending=[1])
    npindex = pdindex.to_numpy()

    ion_position, ion_comp_pos, current_rt, current_mass, mass_diff, kmd_diff, cut_ions, mergegroups = 0, 0, 0, 0, 0, 0, [], {}
    for ions in npindex[0:,0]: #scrolls through ions in order and checks if any subsequent ions fall within time and mass filter range, any ions that are are copied to a list
        current_rt = npindex[ion_position, 2]
        current_mass = npindex[ion_position, 1]
        current_ion = npindex[ion_position, 0]
        ion_comp_pos = ion_position + 1
        if (current_ion not in cut_ions):
            for ions in npindex[ion_comp_pos:, 0]: # the following statement checks if any peaks are within 0.05 min and in the mass filtering window.
                    #The mass filtering window works by checking if the difference of the two ions, when multiplied by two and floored, is even this
                    #corresponds to filtering out ions within 0.5 daltons of a peak or any of its first five isotopic peaks.
                mass_diff = abs((npindex[ion_comp_pos, 1] - current_mass))
                kmd_diff = mass_diff - math.floor(mass_diff)
                if ((npindex[ion_comp_pos, 1] - current_mass) > analysis_params.maxisowin - .4):
                    break    # breaks loop if we are already past the maximum consideration window for isotope shift, saves considerable processsing time.
                if ((abs(npindex[ion_comp_pos, 2]-current_rt) <= analysis_params.RTwin) # RT band
                    and ((npindex[ion_comp_pos, 1] - current_mass) <= analysis_params.maxisowin - .4)
                    and ((math.floor(mass_diff * (1/analysis_params.ringingwin)) % (1/analysis_params.ringingwin) == 0) #band for ringing
                    or ((kmd_diff - .5004 - (math.floor(mass_diff) * .007))  < analysis_params.dimerpeakwin)) #band for doubly charged dimer removal, CHECK TO SEE IF CAN USE MOD FOR THIS
                    and (npindex[ion_comp_pos, 0] not in cut_ions)): # check if ion already removed
                    
                    cut_ions.append(npindex[ion_comp_pos, 0]) #creates or appends merge group to indicate which ions to be merged. Merge not yet implimented
                    if current_ion in mergegroups:
                        mergegroups[current_ion].sources.append(npindex[ion_comp_pos, 0])
                    else:
                        mergegroups[current_ion] = ionmerge(current_ion, npindex[ion_comp_pos, 0])
                ion_comp_pos += 1
        ion_position += 1
    ionfilterlist['relfil'] = ionfilter('', cut_ions)
    ionfilterlist['relfil'].merge = mergegroups

    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = 0)
    iondict['pass_relfil'] = ~iondict.index.isin(ionfilterlist['relfil'].ions)
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header = True, index = True) #saves formatted backup for later use

    return(ionfilterlist)

def mergeions(analysis_params, ionfilters): #because of lack of hybrid indexing (.ix is deprecated) cant use ion name for rows and position index 2: for columns; 
        #need to use col names which is not feasible, find row position based on name (might be best but not sure how to do), or find index tuples with rt and mz. 
        #Implemented the last
    msdata_merged = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [2], index_col = [0])
    mergedic, sourcelist, droplist = {}, [], []
    for target in ionfilters['relfil'].merge:
        targetindex = ((target, msdata_merged.loc[target, 'm/z'], msdata_merged.loc[target, 'Retention time (min)']))
        sourcelist = []
        for source in ionfilters['relfil'].merge[target].sources:
            sourcelist.append((source, msdata_merged.loc[source, 'm/z'], msdata_merged.loc[source, 'Retention time (min)']))
        droplist = droplist + sourcelist
        mergedic[targetindex] = sourcelist
        
    msdata_merged = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [0, 1, 2], index_col = [0, 1, 2])
    for target in mergedic:
        for source in mergedic[target]:
            msdata_merged.loc[target] = msdata_merged.loc[target] + msdata_merged.loc[source]
            msdata_merged.loc[source] #not sure if this is needed
    msdata_merged = msdata_merged.drop(droplist, axis=0)
    msdata_merged.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_merged.csv'), header = True, index = True)
    msdata_merged = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_merged.csv'), sep = ',', header = None, index_col = None)
    msdata_merged.iloc[2,0:3] = ['Compound', 'm/z', 'Retention time (min)']
    msdata_merged.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), header = False, index = False)


def applyfilters(analysis_params, ionfilters):
    msdataout_filtered = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = None, index_col = None) # reopen original data
    for elem in ionfilters:
        msdataout_filtered = listfilter(msdataout_filtered, ionfilters[elem].ions, False)
    msdataout_filtered.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_filtered.csv'), index = False, header = False) # saves output
