"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import pandas as pd
import numpy as np
import filter
import stats
from datetime import datetime
import time
from pathlib import Path

#---Classes---


class groupset:  # parses the ions to be plotted as a specific color based on thier presence in user input sample groups
    """
    Parses the ions to be plotted as a specific color based on their presence in user input sample groups.

    Args:
    - name (str): The name of the group set.
    - query (query_parameters): A query_parameters object.
    - iondictloc (str): The file path to the ion dictionary location.

    Attributes:
    - legendname (str): The legend name of the group set.
    - excl (list of str): The exclusion groups in the group set.
    - incl (list of str): The inclusion groups in the group set.
    - plotcol (str): The plot color of the group set.
    - ionlist (list of str): The ions to be plotted in the group set.
    """
    def __init__(self, name, query, iondictloc):
        self.legendname = query.name
        self.excl = query.excl
        self.incl = query.incl
        self.plotcol = query.colour
    
        iondict = pd.read_csv(iondictloc, sep = ',', header = 0, index_col = 'Compound') #block adds average and median cv to iondict.csv, move elsewhere
        iondict = iondict.loc[iondict['groups'].notna(), 'groups'].to_frame()
        exclgrps = ' ' + '| '.join(self.excl)
        if len(exclgrps)>3: #only runs below line if there is an exclusion group
            iondict = iondict.loc[~iondict['groups'].str.contains(exclgrps), 'groups'].to_frame()#this does not work right if there are no exclusion groups so an artificial one was added
        for group in self.incl:
            iondict = iondict.loc[iondict['groups'].str.contains(' ' + str(group)), 'groups'].to_frame()
        self.ionlist = iondict.index.to_list()
       
class analysis_parameters:
    """
    An empty class that is used as a placeholder to hold analysis parameters.
    
    Attributes:
    - init (str): An initial string.
    """
    def __init__(self):
        self.init = ''


#---Methods---

def start_time(): 
    """Function to start calculating runtime"""
    global initial
    initial = time.time()
    return initial

def stop_time(): 
    """Function to stop calculating runtime and return the elapsed time"""
    final = time.time()
    return(final - initial)

def importdata():
    """Function to import data from files and format it"""
    print('Loading files')
    
    extractmetadata = pd.read_csv(analysis_params.extractmetadatafilename, sep = ',', header = [0], index_col = None) #imports sample/extract metadata
    samplelist = pd.read_csv(analysis_params.samplelistfilename, sep = ',', header = [0], index_col = None) #imports instrument sample list
    combinedmetadata = extractmetadata.set_index('Sample_Code').join(samplelist.set_index('Sample_Code')).reset_index().set_index('Injection') #joins extract metadata and sample list by the sample code, looks like a god line probabaly best to move set index into the import
    msdata = pd.read_csv(analysis_params.filename, sep = ',', header = None, index_col = [0, 1, 2]) #imports feature list
    position = 0
    for elem in msdata.iloc[1]: # itterates over header to format
        msdata.iloc[1, position] = combinedmetadata.loc[msdata.iloc[2, position], 'Sample_Code']
        msdata.iloc[0, position] = combinedmetadata.loc[msdata.iloc[2, position], 'Biological_Group']
        position += 1 # increments current injection index
    
    # Import sample/extract metadata
    extractmetadata = pd.read_csv(analysis_params.extractmetadatafilename, 
                                   sep=',', header=0, index_col=None)
    
    # Import instrument sample list
    samplelist = pd.read_csv(analysis_params.samplelistfilename, 
                              sep=',', header=0, index_col=None)
    
    # Join extract metadata and sample list by the sample code
    combinedmetadata = (extractmetadata.set_index('Sample_Code')
                        .join(samplelist.set_index('Sample_Code'))
                        .reset_index().set_index('Injection'))
                    
    
    # Import feature list
    msdata = pd.read_csv(analysis_params.filename, sep=',', header=None, 
                          index_col=[0, 1, 2])
    
    # Iterate over header to format
    for position, elem in enumerate(msdata.iloc[1]):
        msdata.iloc[1, position] = combinedmetadata.loc[
            msdata.iloc[2, position], 'Sample_Code']
        msdata.iloc[0, position] = combinedmetadata.loc[
            msdata.iloc[2, position], 'Biological_Group']
    
    # Write formatted peak table
    print('Writing formatted peak table')
    msdata.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), 
                   header=False, index=True)
    
    # Import data from formatted peak table
    msdata = pd.read_csv(analysis_params.outputdir / 
                          (analysis_params.filename.stem + '_formatted.csv'), 
                          sep=',', header=[0, 1, 2], index_col=[0])
    
    # Calculate mean of each row and drop rows with mean of 0
    msdataave = msdata.iloc[:, 2:].astype(float)
    msdataave['mean'] = msdataave.mean(axis=1, skipna=True)
    msdata = msdata[msdataave['mean'] != 0]

    # Save formatted peak table and original feature list
    msdata.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), 
                   header=True, index=True)
    msdata.to_csv(analysis_params.outputdir / (analysis_params.filename.name), 
                   header=True, index=True)
    
    # Save feature dictionary with KMD for later use
    iondict = pd.read_csv(analysis_params.outputdir / 
                           (analysis_params.filename.stem + '_formatted.csv'), 
                           sep=',', header=[2], index_col=None).iloc[:,:3]
    iondict['kmd'] = iondict['m/z'] - np.floor(iondict['m/z'])
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=False)


def run_MSFaST(self):
    """
    Runs MSFaST analysis with the given analysis parameters and data.
    
    Args:
    self: Object instance of the MSFaST class.
    
    Returns:
    None
    """
    start_time()

    # Import analysis parameters and data
    global analysis_params
    analysis_params = self.analysis_paramsgui
    importdata()

    # Filtering and error propagation
    print('Filtering data')
    self.ionfilters = {}
    if analysis_params.relfil:
        self.ionfilters = filter.relationalfilter(analysis_params, self.ionfilters)
        if analysis_params.merge:
            filter.mergeions(analysis_params, self.ionfilters)
    if analysis_params.grpave:
        stats.groupave(analysis_params)
        print('Parsing ion lists')
        groupionlists = filter.parsionlists(analysis_params)
    if analysis_params.blnkfltr:
        msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep=',', header=[0, 1, 2], index_col=None)
        msdata = filter.listfilter(msdata, groupionlists[analysis_params.blnkgrp], False)
        msdata = msdata.drop(analysis_params.blnkgrp, axis=1, level=0)
        msdata.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), header=True, index=False)
        iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=0)
        iondict['pass_blnkfil'] = ~iondict.index.isin(groupionlists[analysis_params.blnkgrp])
        iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=True)
    if analysis_params.CVfil:
        self.ionfilters = filter.cvfilter(analysis_params, self.ionfilters, analysis_params.cvthresh)
    if analysis_params.decon:
        self.ionfilters = filter.decon(analysis_params, self.ionfilters)
    filter.applyfilters(analysis_params, self.ionfilters)
    if analysis_params.prperr:
        stats.properr(analysis_params)

    # Store group ion lists for later use
    self.groupionlists = groupionlists

    # Parse ion lists and add filter lists
    groupionlists['cv'] = self.ionfilters['cv'].ions if analysis_params.CVfil else []
    groupionlists['relfil'] = self.ionfilters['relfil'].ions if analysis_params.relfil else []
    groupionlists['insource'] = self.ionfilters['insource'].ions if analysis_params.decon else []

    # Add groups column to iondict csv
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=0, index_col=None)
    iondict['groups'] = ''
    for group in groupionlists:
        iondict.loc[iondict['Compound'].isin(groupionlists[group]), 'groups'] += (' ' + str(group))
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=None)

    # Add default filters to querylist
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=None)
    self.groupsets, self.filtereddfs = {}, {}
    for elem in analysis_params.querylist:
        self.groupsets[elem] = groupset(elem, analysis_params.querydict[elem], analysis_params.outputdir / 'iondict.csv')
        self.filtereddfs[elem] = filter.listfilter(iondict, self.groupsets[elem].ionlist, True)


    #block creates user specified plots some of these can be changed to eliminate a few arguments with data pulled from analysis_params
    if analysis_params.FC:    
        stats.runfc(analysis_params, analysis_params.statstgrps)
    if analysis_params.Ttest:
        stats.runttest(analysis_params, analysis_params.statstgrps, self.groupsets)
    
    #---Analysis info file writing---
    runtime = stop_time()
    msdata_filtered = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_filtered.csv'), sep = ',', header = [0, 1, 2], index_col = [0])
    msdata_header = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_filtered.csv'), sep = ',', header = None, index_col = [0,1,2]).iloc[:3,:].transpose()
    msdata_header.columns = ['Biolgroup', 'Sample', 'Injection']
    
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
    self.unfilteredgroupsets, self.unfiltereddfs = {}, {}
    
    self.analysis_paramsgui = analysis_params
    msdata_unformatted = pd.read_csv(analysis_params.filename, sep = ',', header = [0, 1, 2], index_col = [0, 1, 2]) #imports feature list
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.name), sep = ',', header = [0, 1, 2], index_col = [0, 1, 2])
    msdata_filtered = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_filtered.csv'), sep = ',', header = [0, 1, 2], index_col = [0, 1, 2])
    analysisrec = open(analysis_params.outputdir / 'analysisinfo.txt',"w")
    analysisrec.writelines(['Analysis Date: ' + str(datetime.now()) + '\n',
                            'Runetime: ' + str(round(runtime, 2)) + ' seconds\n',
                            'Input file: ' + str(analysis_params.filename) + '\n',
                            'Sample list: ' + str(analysis_params.samplelistfilename) + '\n',
                            'Extract metadata file: ' + str(analysis_params.extractmetadatafilename) + '\n',
                            'Number of injections: ' + str(msdata_header['Injection'].nunique()) + '\n',
                            'Number of samples: ' + str(msdata_header['Sample'].nunique())  + '\n',
                            'Number of biological groups: ' + str(msdata_header['Biolgroup'].nunique())  + '\n',
                            '\n',
                            '\n',
                            '---Filtering---\n',
                            '-CV filtering-\n',
                            'CV threshold: ' + str(analysis_params.cvthresh) + '\n',
                            '\n',
                            '-Relative filtering-\n',
                            'Ringing window: ' + str(analysis_params.ringingwin) + '\n',
                            'Isotopic peak window: ' + str(analysis_params.isopeakwin) + '\n',
                            'Dimer filter window: ' + str(analysis_params.dimerpeakwin) + '\n',
                            'RT window: ' + str(analysis_params.RTwin) + '\n',
                            'max isotopic peak shift: ' + str(analysis_params.maxisowin) + '\n',
                            '\n',
                            'Total features: ' + str(len(msdata.index)) + '\n'])
    

    text = ''
    if self.analysis_paramsgui.relfil:
        text += 'Features failing peak correction filtering: ' + str(len(self.ionfilters['relfil'].ions)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.ionfilters['relfil'].ions) / len(msdata_unformatted.index), 2)) + '%\n'
    if self.analysis_paramsgui.blnkfltr: #FIX THIS REF TO "BLANKS"
        text += 'Features failing blank filtering: ' + str(len(self.groupionlists['Blanks'])) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.groupionlists['Blanks']) / len(msdata_unformatted.index), 2)) + '%\n'
    if self.analysis_paramsgui.decon:
        text += 'Features failing blank filtering: ' + str(len(self.ionfilters['insource'].ions)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.ionfilters['insource'].ions) / len(msdata_unformatted.index), 2)) + '%\n'
    if self.analysis_paramsgui.CVfil:
        text += 'Features failing CV filtering: ' + str(len(self.ionfilters['cv'].ions)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.ionfilters['cv'].ions) / len(msdata_unformatted.index), 2)) + '%\n'
    text += 'Features failing any filters: ' + str(len(msdata_unformatted.index) - len(msdata_filtered.index)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * (len(msdata_unformatted.index) - len(msdata_filtered.index)) / len(msdata_unformatted.index), 2)) + '%\n'
    text += 'Features passing all filters: ' + str(len(msdata_filtered.index)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(msdata_filtered.index) / len(msdata_unformatted.index), 2)) + '%\n'
    
    analysisrec.writelines([text,
                            '\n',
                            '\n',
                            '---Graphing Parameters---\n',
                            'Filters: \n'])
    
    for elem in analysis_params.graphfilters.split(' '):
        analysisrec.write(elem + '\n')
    
    analysisrec.writelines(['\n',
                            '-Groups-\n'])
    
    for elem in analysis_params.querylist:
        analysisrec.write(elem + '\n')
    
    analysisrec.writelines(['\n',
                            '-Plots generated-\n',
                            'RT/mz: ' + str(analysis_params.MZRTplt) + '\n',
                            'RT/mz/FC: ' + str(analysis_params.FC3Dplt) + ' ' + str(analysis_params.statstgrps) + '\n',
                            'KMD/mz ' + str(analysis_params.KMD) + '\n',
                            #'KMD/mz/RT ' + str(analysis_params.___) + '\n',
                            'PCA unfitlered: ' + str(analysis_params.PCA) + '\n',
                            'PCA filtered: ' + str(analysis_params.PCA) + '\n',
                            'Dendrogram (ward) unfiltered: ' + str(analysis_params.Dendrogram) + '\n',
                            'Dendrogram (ward) Filtered: ' + str(analysis_params.Dendrogram) + '\n',
                            'Volcano plot: ' + str(analysis_params.Volcanoplt) + ' ' + str(analysis_params.statstgrps) + '\n',])
    analysisrec.close()
