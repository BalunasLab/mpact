"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import pandas as pd
import numpy as np
import math
import scipy.cluster.hierarchy as spc
import mspwriter

class ionmerge:
    """
    A class representing a target ion and sources to merge for mispicked filter.

    Parameters:
        target (str): The target ion to merge.
        sources (list): A list of sources to merge with the target ion.

    Attributes:
        target (str): The target ion to merge.
        sources (list): A list of sources to merge with the target ion.
    """
    def __init__(self, target, sources):
            self.target = target
            self.sources = []
            self.sources.append(sources)

class ionfilter: 
        """
        A class representing a general ionfilter with parameters and a list of ions to remove.
        
        Parameters:
            parameters (dict): A dictionary of parameters for the ionfilter.
            ionlist (list): A list of ions to remove.
        
        Attributes:
            params (dict): A dictionary of parameters for the ionfilter.
            ions (list): A list of ions to remove.
            merge (list): A list of ionmerge objects.
        """
        def __init__(self, parameters, ionlist):
            self.params = parameters
            self.ions = ionlist
            self.merge = []
            

        
def reformatcorr(corr): #reformat to for pos in range(1:corr.shape[0]) or something like that
    """
    Reformats a correlation matrix to generate a list from sequential columns.
    
    Parameters:
        corr (pd.DataFrame): The correlation matrix to be reformatted.
    
    Returns:
        np.ndarray: A reformatted array derived from the input correlation matrix.
    """
    corr = corr.to_numpy()
    reformatted = corr[1:,0]
    pos = 1
    while pos < corr.shape[0]:
        reformatted = np.append(reformatted, corr[pos+1:,pos], axis=0)
        pos = pos + 1
    reformatted = 1-np.where(reformatted<0, 0, reformatted)
    return(reformatted)




def decon(analysis_params, ionfilters):
    """
    Perform peak deconvolution on the data and update the ion filters and dictionary.
    
    This function reads in formatted data and performs peak deconvolution using the correlation clustering method. It
    then groups peaks into clusters, generates a list of precursor and fragment ions, and updates the ion filters and
    dictionary. Finally, the function writes the formatted data back out to disk.
    
    Parameters:
        analysis_params (object): Analysis parameters.
        ionfilters (dict): Dictionary of ion filters.
    
    Returns:
        dict: Updated dictionary of ion filters.
    """
    # Read in data
    msdata_ind = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'),
                             sep=',', header=[2], index_col=[0, 1]).iloc[:, :1]
    rtlist = msdata_ind['Retention time (min)'].unique()
    msdata_ind = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'),
                             sep=',', header=[2], index_col=[0]).iloc[:, :2]
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'),
                         sep=',', header=[2], index_col=[0]).iloc[:, 2:]

    # Initialize variables
    singleslist = []
    insourcelist = []
    clusterlist = []
    clusterdfs = []
    filtereddf = msdata_ind
    ftrgrps = {}
    mergegroups = {}

    # Loop through retention times
    for elem in rtlist:
        filtereddf = msdata_ind.loc[msdata_ind.iloc[:, 1] == elem, :]

        if len(filtereddf.index) == 1:
            singleslist.append(filtereddf.index.to_list()[0])
        else:
            # Perform deconvolution
            unseplist = filtereddf.index.tolist()
            filtereddf2 = msdata.loc[unseplist, :].transpose()
            corr = filtereddf2.corr()
            corr2 = reformatcorr(corr)
            linkage = spc.linkage(corr2, method='complete')
            np.clip(linkage, 0, None, linkage)
            idx = spc.fcluster(linkage, 1 - analysis_params.deconthresh, 'distance')

            # Group peaks by cluster
            decongroups = {}
            for group in range(1, max(idx) + 1):
                decongroups[group] = []
            for peak in range(0, idx.shape[0]):
                if peak < len(unseplist):
                    decongroups[idx[peak]].append(unseplist[peak])

            # Append groups to appropriate lists
            for group in decongroups:
                if len(decongroups[group]) == 1:
                    singleslist.append(decongroups[group][0])
                else:
                    clusterlist.append(decongroups[group])
                    tempdf = msdata_ind.loc[decongroups[group]].sort_values(by=['m/z'], ascending=False)
                    if len(tempdf.index.to_list()) > 0:
                        precursor = tempdf.index.to_list()[0]
                        fragments = tempdf.index.to_list()[1:]
                        singleslist.append(precursor)
                        insourcelist += fragments
                        clusterdfs.append(tempdf)
                        mergegroups[precursor] = ionmerge(precursor, fragments)


    # Write out data
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'),
                         sep=',', header=[0, 1, 2], index_col=[0])
    msdata = msdata.loc[singleslist]
    msdata.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'),
                  header=True, index=True)

    # Update ion filters
    ionfilters['insource'] = ionfilter('', insourcelist)
    ionfilters['insource'].merge = mergegroups

    # Update ion dictionary
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=0)
    iondict['pass_insource'] = ~iondict.index.isin(ionfilters['insource'].ions)
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=True)
    
    # Convert ion filters to MSP format
    mspwriter.convert_to_msp(ionfilters['insource'], analysis_params)
    
    return ionfilters

# -----CV Filtering-----
def listfilter(msdata, ionlist, include):
    """
    Filters msdata based on the ions in ionlist.

    Parameters:
        msdata (pandas.DataFrame): Dataframe to filter.
        ionlist (list): List of ions to filter by.
        include (bool): If True, keep ions in ionlist. If False, remove ions in ionlist.

    Returns:
        pandas.DataFrame: Filtered dataframe.
    """
    if include:
        msdata = msdata[msdata.iloc[:, 0].isin(ionlist)]
    else:
        msdata = msdata[~msdata.iloc[:, 0].isin(ionlist)]
    return msdata

def groupfilter(group, msdata_blankfilterg, analysis_params):
    """
    Filters ions in msdata_blankfilterg based on presence in group.

    Parameters:
        group (str): Group to filter by.
        msdata_blankfilterg (pandas.DataFrame): Dataframe to filter.
        analysis_params (object): Analysis parameters.

    Returns:
        list: List of filtered ions.
    """
    # Filters ions based on group presence > 100 ions/abundance
    msdata_blankfilterg = msdata_blankfilterg[msdata_blankfilterg[group] > analysis_params.blankfilthresh]
    msdata_blankfilterg = msdata_blankfilterg.reset_index()
    # Returns filtered dataframe index as list
    groupfilterlist = msdata_blankfilterg.iloc[0:,0].tolist()
    return groupfilterlist

def parsionlists(analysis_params):
    """
    Parses lists of ions present in each group.

    Parameters:
        analysis_params (object): Analysis parameters.

    Returns:
        dict: Dictionary of group ion lists.
    """
    msdata_blankfilterg = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_groupaverages.csv'), sep = ',', header = [0], index_col = [0, 1, 2, 3]).unstack()
    msdata_blankfilterg.columns = msdata_blankfilterg.columns.droplevel()
    msdata_blankfilterg['max'] = msdata_blankfilterg.max(numeric_only=True, axis=1)
    for column in msdata_blankfilterg:
        msdata_blankfilterg[column] = msdata_blankfilterg[column] / msdata_blankfilterg['max']
    msdata_blankfilterg = msdata_blankfilterg.drop(columns=['max'])
    biolgroups = msdata_blankfilterg.columns.tolist()
    groupionlists = {}
    for group in biolgroups:
        groupionlists[group] = groupfilter(group, msdata_blankfilterg, analysis_params)
    return groupionlists

def cvfilter(analysis_params, ionfilterlist, threshold):
    """
    Filters ions based on the coefficient of variation (CV).
    """
    print('Running CV filter')
    
    # Import data and calculate CV
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'),
                         sep=',', header=[0, 1, 2], index_col=[0, 1, 2]).stack([0, 1, 2])
    msdata_cv = (msdata.groupby(level=[0, 1, 2, 3, 4]).std() / msdata.groupby(level=[0, 1, 2, 3, 4]).mean())
    msdatameancv = msdata_cv.groupby(level=0).mean().to_frame()
    msdatamediancv = msdata_cv.groupby(level=0).median().to_frame()
    
    # Add average and median CV to iondict.csv
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=0)
    iondict['average CV'] = msdatameancv.iloc[:, 0]
    iondict['median CV'] = msdatamediancv.iloc[:, 0]
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=True)

    # Determine ions to keep and reject based on CV threshold
    msdata_filtered = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'),
                                  sep=',', header=[0, 1, 2], index_col=[0])
    ionlist = msdata_filtered.index.tolist()
    iondict = iondict[iondict[analysis_params.cvparam] < threshold]
    cvkeeplist = iondict.index.tolist()
    cvfilterlist = list(set(ionlist) - set(cvkeeplist))
    ionfilterlist['cv'] = ionfilter(analysis_params.cvthresh, cvfilterlist)

    # Update iondict with pass_cvfil column and save
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=0)
    iondict['pass_cvfil'] = ~iondict.index.isin(ionfilterlist['cv'].ions)
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=True)
    
    return ionfilterlist

# -----Deringing and relational filter algorithm-----
def relationalfilter(analysis_params, ionfilterlist):
    """
    Implements a de-ringing and relational filtering algorithm for MS data.

    Parameters:
        analysis_params (object): Analysis parameters.
        ionfilterlist (dict): Dictionary of ion filters.

    Returns:
        dict: Dictionary of ion filters.

    The algorithm works by first sorting the MS data by m/z, and then iterating over the data one ion at a time, 
    comparing each ion to all subsequent ions that fall within a certain mass and retention time window. 
    Ions that meet certain criteria are then merged into a single ion using the ionmerge class. 

    The filtering criteria includes:
    - A mass difference of less than a specified value
    - A retention time difference of less than a specified value
    - A difference between the mass difference and its floor when multiplied by a factor, indicating the presence of ring artifacts
    - A difference between the mass difference and 0.5004 when accounting for the doubly-charged dimer, indicating the presence of dimer peaks

    The function returns a dictionary of ion filters, with the 'relfil' filter containing a list of ions to remove, 
    and a 'merge' attribute which contains the merge groups (as an ionmerge object) that specify which ions to merge.
    """
    
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


def mergeions(analysis_params, ion_filters):
    """
    Merges source to target ion abundances for mispicked peak filtering.
    
    Parameters:
        analysis_params (object): Analysis parameters.
        ion_filters (dict): Dictionary of ion filters.
    
    Returns:
        None
    """
    # Read in the data
    msdata_merged = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep=',', header=[2], index_col=[0])

    # Initialize variables
    merge_dict = {}
    source_list = []
    drop_list = []

    # Loop through each target ion and its associated sources
    for target in ion_filters['relfil'].merge:
        target_index = (target, msdata_merged.loc[target, 'm/z'], msdata_merged.loc[target, 'Retention time (min)'])
        source_list = []
        for source in ion_filters['relfil'].merge[target].sources:
            source_list.append((source, msdata_merged.loc[source, 'm/z'], msdata_merged.loc[source, 'Retention time (min)']))
        drop_list += source_list
        merge_dict[target_index] = source_list
        
    # Merge the ions in the data frame
    msdata_merged = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep=',', header=[0, 1, 2], index_col=[0, 1, 2])
    for target in merge_dict:
        for source in merge_dict[target]:
            msdata_merged.loc[target] += msdata_merged.loc[source]

    # Drop the source ions
    msdata_merged = msdata_merged.drop(drop_list, axis=0)

    # Save the merged data frame
    msdata_merged.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_merged.csv'), header=True, index=True)

    # Format the merged data frame and save it
    msdata_merged = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_merged.csv'), sep=',', header=None, index_col=None)
    msdata_merged.iloc[2, 0:3] = ['Compound', 'm/z', 'Retention time (min)']
    msdata_merged.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), header=False, index=False)

def applyfilters(analysis_params, ion_filters):
    """
    Applies a list of ion filters to the data.
    
    Parameters:
        analysis_params (object): Analysis parameters.
        ion_filters (dict): Dictionary of ion filters.
    
    Returns:
        None
    """
    ms_data_out_filtered = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep=',', header=None, index_col=None)  # reopen original data
    for elem in ion_filters:
        ms_data_out_filtered = listfilter(ms_data_out_filtered, ion_filters[elem].ions, False)
    ms_data_out_filtered.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_filtered.csv'), index=False, header=False)  # saves output
    
