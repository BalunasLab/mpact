"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import pandas as pd
import numpy as np
from scipy import stats
from filter import listfilter

def tstat(m1, sd1, n1, m2, sd2, n2):
    numerator = m1 - m2
    den1 = (sd1**2/n1).replace([np.inf, -np.inf, np.nan], 0)
    den2 = (sd2**2/n2).replace([np.inf, -np.inf, np.nan], 0)
    denominator = (den1 + den2)**0.5
    return(np.absolute(numerator/denominator))

def ws(sd1, n1, sd2, n2): #welche satterthwaite
    s1 = sd1/(n1**.5)
    s2 = sd2/(n2**.5)
    numerator = (s1**2/n1 + s2**2/n2)**2
    den1 = s1**4/((n1**2)*(n1-1))
    den2 = s2**4/((n2**2)*(n2-1))
    denominator = den1.replace([np.inf, -np.inf, np.nan], 0) + den2.replace([np.inf, -np.inf, np.nan], 0)
    return(numerator/denominator)

def groupave(analysis_params):
    #OVERALL AVERAGE CALCULATION
    print('Averaging groups')
    #the following finds technical averages and RSDs
    msdata_errprop = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep = ',', header = [0, 1, 2], index_col = [0, 1, 2]) #imports data
    msdata_errprop_tidy = msdata_errprop.stack([0,1,2])
    msdata_errprop_mean = (msdata_errprop_tidy.groupby(level = [0,1,2,3,4]).mean())
    msdata_errprop = msdata_errprop_mean.groupby(level = [0,1,2,3]).mean().to_frame()
    msdata_errprop.columns = ['average']
    msdata_errprop['biolRSD'] = msdata_errprop_mean.groupby(level = [0,1,2,3]).std().fillna(0) / msdata_errprop_mean.groupby(level = [0,1,2,3]).mean()
    msdata_errprop['bioln'] = msdata_errprop_mean.groupby(level = [0,1,2,3]).count()
    msdata_errprop_sd = (msdata_errprop_tidy.groupby(level = [0,1,2,3,4]).std() / msdata_errprop_tidy.groupby(level = [0,1,2,3,4]).mean()).to_frame()
    msdata_errprop['techRSD'] = msdata_errprop_sd.groupby(level = [0,1,2,3]).mean()
    msdata_errprop_n = msdata_errprop_tidy.groupby(level = [0,1,2,3,4]).count()
    msdata_errprop['techn'] = msdata_errprop_n.groupby(level = [0,1,2,3]).mean()

    msdata_errprop.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'), header = True, index = True)
    msdata_errprop_grpav = msdata_errprop.loc[:, msdata_errprop.columns.intersection(['average'])] # cuts all columns besides CV/rsd
    msdata_errprop_grpav.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_groupaverages.csv'), header = True, index = True)


def properr(analysis_params): #error propagation code, could use some cleanup for efficiency/readibility
    print('Propagating error')
    msdata_errprop = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'), sep = ',', header = [0], index_col = [0, 1, 2, 3])
    msdata_errprop['combRSD']=(msdata_errprop['techRSD']**2+msdata_errprop['biolRSD']**2)**.5 #calculates combides RSD based on RSS formula. change to np.sqrt instead of **.5
    msdata_errprop['combASD']=msdata_errprop['combRSD']*msdata_errprop['average'] # finds over absolute combinded SD
    msdata_errprop['combASD'][np.isnan(msdata_errprop['combASD'])] = 0 # add this line if ions exclusive to one group or the other should be shown in volcano plot
    msdata_errprop['biolRSD'][np.isnan(msdata_errprop['biolRSD'])] = 0
    msdata_errprop['techRSD'][np.isnan(msdata_errprop['techRSD'])] = 0
    #msdata_errprop['neff'] = msdata_errprop['bioln'] * msdata_errprop['techn'] * (msdata_errprop['techRSD']**2 + msdata_errprop['biolRSD']**2) / (msdata_errprop['bioln'] * msdata_errprop['techRSD']**2 + msdata_errprop['techn'] * msdata_errprop['biolRSD']**2 )
    msdata_errprop['neff'] = (ws(msdata_errprop['techRSD'],  msdata_errprop['techn'], msdata_errprop['biolRSD'], msdata_errprop['bioln']) + 1).replace([np.inf, -np.inf, np.nan], 0)
    
    msdata_errprop=msdata_errprop.unstack()
    msdata_errprop.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'), sep = ',', index = True, header = True)

def runfc(analysis_params, statstgrps): #calculates fold change between statstgrps, need to change to just pull statstgrps from analysisparams
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
    maxval=100
    minval=.01
    msdata_errprop = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_groupaverages.csv'), sep = ',', header = [0], index_col = [0, 1, 2, 3]).unstack()
    msdata_errprop.columns = msdata_errprop.columns.droplevel()
    maxvals = msdata_errprop.max(axis=1) #the max stuff is used to base point opacity based on abundance, have to put in a better location than this
    msdata_errprop = msdata_errprop.loc[:, msdata_errprop.columns.intersection(statstgrps)]
    msdata_errprop['FC']=msdata_errprop[statstgrps[0]]/msdata_errprop[statstgrps[1]]
    msdata_errprop['FC'][msdata_errprop['FC'] >= maxval] = maxval
    msdata_errprop['FC'][msdata_errprop['FC'] <= minval] = minval
    msdata_errprop['max'] = maxvals # this has to be done before resetting the index or else tuple/string expectation error thrown
    msdata_errprop = msdata_errprop.reset_index([1,2])
    iondict['fc'] = msdata_errprop['FC']
    iondict['max'] = msdata_errprop['max']
    iondict['logmax'] = np.log10(iondict['max']) 
    #iondict['logfc'] = np.log2(iondict['fc']) maybe include this later, can replace relevant line in fc3d
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header = True, index = True) #saves formatted backup for later use

def runttest(analysis_params, statstgrps, groupsets):
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
    minval = .00001
    msdata_errprop = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'), sep = ',', header = [0, 1], index_col = [0, 1, 2])
    msdata_teststats = msdata_errprop
    msdata_teststats['T'] = tstat(msdata_teststats[('average',statstgrps[0])], msdata_teststats[('combASD',statstgrps[0])], msdata_teststats[('neff',statstgrps[0])], msdata_teststats[('average',statstgrps[1])], msdata_teststats[('combASD',statstgrps[1])], msdata_teststats[('neff',statstgrps[1])])
    #msdata_teststats['T'] = np.absolute((msdata_teststats[('average',statstgrps[0])] - msdata_teststats[('average',statstgrps[1])])/(((msdata_teststats[('combASD',statstgrps[0])]**2)/msdata_teststats[('neff',statstgrps[0])] + (msdata_teststats[('combASD',statstgrps[1])]**2)/msdata_teststats[('neff',statstgrps[1])])**.5))
    msdata_teststats['deg'] = msdata_teststats[('neff',statstgrps[0])] + msdata_teststats[('neff',statstgrps[1])] - 2 #need to look at this in more detail... see https://en.wikipedia.org/wiki/Student%27s_t-test for welches t test
    msdata_teststats['p'] =(1-stats.t.cdf(msdata_teststats['T'],msdata_teststats['deg'])) * 2 # THIS WAS A PROBLEM NEEDED TO MULTIPLY BY 2!
    msdata_teststats['p'][msdata_teststats['p'] <= minval] = minval
    msdata_teststats['logp'] = np.log10(msdata_teststats['p']) 
    
    msdata_teststats = msdata_teststats.reset_index([1,2])
    msdata_teststats.to_csv('msdata_teststats_test.csv', header = True, index = True) #maybe can be removed, i think this for checkpoint testing and was not removed but don't recall
    iondict['-logp'] = -msdata_teststats['logp']
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header = True, index = True) #saves formatted backup for later use
    
    
    #FDR correction, perhaps move to a new seperate method
    
    #iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = None) # original call for looped method i pulled from volcanoplt method, may need to use this type of line where index col is in df
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_filtered.csv'), sep = ',', header = [2], index_col = 0).index.tolist()
    iondict = iondict.loc[msdata].reset_index() # may have solved above noted issue with reset_index call, above line to filter indict based on filtered msdata needs ion name as index, but listfilter method needs it as first col of df
    position = 0

    plottedions = []
    for elem in analysis_params.querylist: #creates list of all ions to be plotted and tested, should be done differently, see remarks on ttest call in msfast module
        plottedions = list(set(plottedions + groupsets[elem].ionlist))
    iondict = listfilter(iondict, plottedions, True)

    
    
    iondict['p'] = 10**(-iondict['-logp'])
    iondict = iondict.sort_values(by=['p'])
    numions = len(iondict[iondict['p'] <= 1].index)
    #print('numions: ' + str(numions))
    iondict['qval'] = iondict.reset_index().index + 1
    iondict['qval'] =  iondict['p']*numions/iondict['qval']
    iondict = iondict.sort_values(by=['p'], ascending=False)
    minval=1
    qvals = iondict['qval'].tolist()
    for pos in range(0,len(qvals)):
        if qvals[pos] < minval:
            minval = qvals[pos]
        else:
            qvals[pos] = minval
    
    iondict['qval'] = qvals
    iondict['-logq'] = -np.log10(iondict['qval']) 
    
    iondict = iondict.set_index('Compound')
    iondict.to_csv('qdata.csv', index = True, header = True) # will want to remove this checkpoint at some point

    iondict2 = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
    iondict2['-logq'] = np.nan
    iondict2.loc[iondict.index.tolist(),'-logq'] = iondict['-logq']
    iondict2.to_csv(analysis_params.outputdir / 'iondict.csv', header = True, index = True) #saves formatted backup for later use