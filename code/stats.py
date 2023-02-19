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
    print('Averaging groups')
    # Load data
    msdata_errprop = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_formatted.csv'), sep=',', header=[0, 1, 2], index_col=[0, 1, 2])

    # Find technical averages and RSDs
    msdata_errprop_tidy = msdata_errprop.stack([0, 1, 2])
    msdata_errprop_mean = msdata_errprop_tidy.groupby(level=[0, 1, 2, 3, 4]).mean()
    msdata_errprop_mean = msdata_errprop_mean.groupby(level=[0, 1, 2, 3]).mean().to_frame()
    msdata_errprop_mean.columns = ['average']
    msdata_errprop_mean['biolRSD'] = msdata_errprop_tidy.groupby(level=[0, 1, 2, 3]).std().fillna(0) / msdata_errprop_tidy.groupby(level=[0, 1, 2, 3]).mean()
    msdata_errprop_mean['bioln'] = msdata_errprop_tidy.groupby(level=[0, 1, 2, 3]).count()
    msdata_errprop_sd = (msdata_errprop_tidy.groupby(level=[0, 1, 2, 3, 4]).std() / msdata_errprop_tidy.groupby(level=[0, 1, 2, 3, 4]).mean()).to_frame()
    msdata_errprop_mean['techRSD'] = msdata_errprop_sd.groupby(level=[0, 1, 2, 3]).mean()
    msdata_errprop_n = msdata_errprop_tidy.groupby(level=[0, 1, 2, 3, 4]).count()
    msdata_errprop_mean['techn'] = msdata_errprop_n.groupby(level=[0, 1, 2, 3]).mean()

    # Save summary data and group averages
    msdata_errprop_mean.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'), header=True, index=True)
    msdata_errprop_grpav = msdata_errprop_mean.loc[:, msdata_errprop_mean.columns.intersection(['average'])]
    msdata_errprop_grpav.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_groupaverages.csv'), header=True, index=True)

def properr(analysis_params):
    print('Propagating error')
    msdata_errprop = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'),
                                 sep=',', header=[0], index_col=[0, 1, 2, 3])

    # Calculate combined RSD and absolute combined SD
    msdata_errprop['combRSD'] = np.sqrt(msdata_errprop['techRSD'] ** 2 + msdata_errprop['biolRSD'] ** 2)
    msdata_errprop['combASD'] = msdata_errprop['combRSD'] * msdata_errprop['average']

    # Set NaN values to 0
    msdata_errprop[['combASD', 'biolRSD', 'techRSD']] = msdata_errprop[['combASD', 'biolRSD', 'techRSD']].fillna(0)

    # Calculate effective sample size and replace infinite and NaN values with 0
    msdata_errprop['neff'] = (ws(msdata_errprop['techRSD'], msdata_errprop['techn'], msdata_errprop['biolRSD'],
                                 msdata_errprop['bioln']) + 1).replace([np.inf, -np.inf, np.nan], 0)

    msdata_errprop = msdata_errprop.unstack()
    msdata_errprop.to_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'),
                           sep=',', index=True, header=True)
    
    
def runfc(analysis_params, statstgrps):
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
    # Load iondict and data
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=[0])
    msdata_errprop = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_summarydata.csv'), sep=',', header=[0, 1], index_col=[0, 1, 2])

    # Set minimum p-value
    minval = 0.00001
        
    # Calculate t-test statistics
    msdata_teststats = msdata_errprop
    msdata_teststats['T'] = tstat(msdata_teststats[('average', statstgrps[0])], msdata_teststats[('combASD', statstgrps[0])], msdata_teststats[('neff', statstgrps[0])], msdata_teststats[('average', statstgrps[1])], msdata_teststats[('combASD', statstgrps[1])], msdata_teststats[('neff', statstgrps[1])])
    msdata_teststats['deg'] = msdata_teststats[('neff', statstgrps[0])] + msdata_teststats[('neff', statstgrps[1])] - 2
    msdata_teststats['p'] = (1 - stats.t.cdf(msdata_teststats['T'], msdata_teststats['deg'])) * 2
    msdata_teststats['p'][msdata_teststats['p'] <= minval] = minval
    msdata_teststats['logp'] = np.log10(msdata_teststats['p']) 
    
    # Save msdata_teststats
    msdata_teststats = msdata_teststats.reset_index([1, 2])
    msdata_teststats.to_csv('msdata_teststats_test.csv', header=True, index=True)
    
    # Update iondict with -logp
    iondict['-logp'] = -msdata_teststats['logp']
    iondict.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=True)
    
    # Load iondict and msdata
    iondict = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=[0])
    msdata = pd.read_csv(analysis_params.outputdir / (analysis_params.filename.stem + '_filtered.csv'), sep=',', header=[2], index_col=0).index.tolist()
    
    # Filter iondict based on msdata
    iondict = iondict.loc[msdata].reset_index()
    
    # Create list of ions to plot and test
    plottedions = []
    for elem in analysis_params.querylist:
        plottedions = list(set(plottedions + groupsets[elem].ionlist))
    
    # Filter iondict based on plottedions
    iondict = listfilter(iondict, plottedions, True)
    
    # Compute p-values for each ion
    iondict['p'] = 10 ** (-iondict['-logp'])
    
    # Sort ions by p-value
    iondict = iondict.sort_values(by=['p'])
    
    # Compute q-values for each ion
    num_ions = len(iondict[iondict['p'] <= 1])
    iondict['qval'] = iondict.reset_index().index + 1
    iondict['qval'] = iondict['p'] * num_ions / iondict['qval']
    iondict = iondict.sort_values(by=['p'], ascending=False)
    
    # Compute minimum q-value
    min_qval = 1
    qvals = iondict['qval'].tolist()
    for pos in range(len(qvals)):
        if qvals[pos] < min_qval:
            min_qval = qvals[pos]
        else:
            qvals[pos] = min_qval
    
    # Compute -logq for each ion
    iondict['qval'] = qvals
    iondict['-logq'] = -np.log10(iondict['qval'])
    
    # Save results to CSV files
    iondict = iondict.set_index('Compound')
    iondict.to_csv('qdata.csv', index=True, header=True)
    iondict2 = pd.read_csv(analysis_params.outputdir / 'iondict.csv', sep=',', header=[0], index_col=[0])
    iondict2['-logq'] = np.nan
    iondict2.loc[iondict.index.tolist(), '-logq'] = iondict['-logq']
    iondict2.to_csv(analysis_params.outputdir / 'iondict.csv', header=True, index=True)