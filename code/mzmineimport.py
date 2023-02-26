"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""


import pandas as pd
import numpy as np
from pathlib import Path


def format_check(parent):
    """
    Check if the file has the right format, and if not, reformat it.
    """
    try:
        if parent.filename.suffix == '.txt':
            reformat_msdial(Path(parent.filename))
            parent.filename = Path(str(parent.filename)[:-4] + '.csv')

            
        if parent.filename.suffix == '.csv':
            msdata = pd.read_csv(parent.filename, sep = ',', header = None, index_col = None) #imports feature list
            if msdata.iloc[0, 0] == 'row ID':
                reformat_mzmine(Path(parent.filename))
            if msdata.iloc[0, 0] == 'Bucket label':
                reformat_metaboscape(Path(parent.filename))
                
            msdata = pd.read_csv(Path(parent.filename), sep = ',', header = [0,1,2], index_col = [0]) #imports data
            if len(msdata[~msdata.index.duplicated()].index) > 0:
                rename_duplicates(Path(parent.filename))
            
    except Exception:
        pass
        return()


def reformat_metaboscape(file):
    """Reformat a file from the Metaboscape software.
    
    Args:
    - file (Path): the path of the file to reformat
    """
    data = pd.read_csv(file, sep = ',', header = None, index_col = None)
    data.iloc[0:3, 0] = ('','','Compound')
    data.iloc[0:3, 1] = ('','','Retention time (min)')
    data.iloc[0:3, 2] = ('','','m/z')
    
    mz = list(data.iloc[:,2])
    data.iloc[:,2] = data.iloc[:,1]
    data.iloc[:,1] = mz
    
    injections = list(data.iloc[0,3:])
    groups = list(data.iloc[1,3:])
    samples = list(data.iloc[2,3:])
    
    data.iloc[0,3:] = groups
    data.iloc[1,3:] = samples
    data.iloc[2,3:] = injections
    
    data=data.drop(data.columns[3:5], axis=1)
    data.to_csv(file, header = False, index = False) #saves formatted backup for later use This line might break on import of new files...
    data = pd.read_csv(file, sep = ',', header = [0,1,2], index_col = [0]) #imports data
    
    data.index = data.index + data.groupby(level=0).cumcount().astype(str).replace('0','')
    data.to_csv(file, header = True, index = True) #saves formatted backup for later use


def reformat_mzmine(file):
    """Reformat a file from the MZmine software.
    
    Args:
    - file (Path): the path of the file to reformat
    """
    data = pd.read_csv(file, sep = ',', header = None, index_col = None)
    data.iloc[0, 0] = 'Compound'
    data.iloc[0, 1] = 'm/z'
    data.iloc[0, 2] = 'Retention time (min)'
    
    xpos = 3
    for elem in data.iloc[0,3:]:
        data.iloc[0,xpos]=data.iloc[0,xpos].split()[0][:-4]
        xpos += 1
        
    df1 = pd.DataFrame([[np.nan] * len(data.columns)], columns=data.columns)
    data = df1.append(data, ignore_index=True)
    data = df1.append(data, ignore_index=True)
    data.to_csv(file, header = False, index = False) #saves formatted backup for later use


def reformat_msdial(file):
    """Reformat a file from the MS-DIAL software.
    
    Args:
    - file (Path): the path of the file to reformat
    """
    database = pd.read_csv(file, sep = '\t', header = None, index_col = None) #imports data
    database.iloc[:,3] = database.iloc[:,2]
    database.iloc[:,2] = database.iloc[:,1]
    database.iloc[:,1] = database.iloc[:,3]
    headser = database.iloc[3,:] == 'Stdev'
    cutlen = len(headser[headser == True]) * 2 #cut cols for stdev and average
    database2 = database.iloc[:,0:3].join(database.iloc[:,32: -cutlen])
    database2.iloc[2,:] = database2.iloc[1,:]
    database2.iloc[3,:] = database2.iloc[1,:]
    database2 = database2.iloc[2:,:]
    database2.iloc[2,:3] = ['Compound', 'm/z', 'Retention time (min)']
    database2.to_csv(file.parent / (str(file.stem) + '.csv'), header = False, index = False) #saves formatted backup for later use This line might break on import of new files...
    database = pd.read_csv(file.parent / (str(file.stem) + '.csv'), sep = ',', header = [0,1,2], index_col = None) #imports data
    database.iloc[:,0] = database.iloc[:,2].astype(str)+"_"+database.iloc[:,1].astype(str)
    database.to_csv(file.parent / (str(file.stem) + '.csv'), header = True, index = False) #saves formatted backup for later use This line might break on import of new files...

def rename_duplicates(file):
    """Rename duplicate entries in the file's index to make them unique.

    Args:
    - file (Path): the path of the file to reformat
    """
    data = pd.read_csv(file, sep = ',', header = [0,1,2], index_col = [0]) #imports data
    
    data.index = data.index + data.groupby(level=0).cumcount().astype(str).replace('0','')
    data.to_csv(file, header = True, index = True) #saves formatted backup for later use