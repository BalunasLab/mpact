# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:37:27 2021

@author: Xanadu
"""
import pandas as pd
import numpy as np
from pathlib import Path


def format_check(parent):
    try:
        if parent.filename.suffix == '.txt':
            reformat_msdial(Path(parent.filename))
            
        if parent.filename.suffix == '.csv':
            msdata = pd.read_csv(parent.filename, sep = ',', header = None, index_col = None) #imports feature list
            if msdata.iloc[0, 0] == 'row ID':
                reformat_mzmine(Path(parent.filename))
                parent.filename = str(parent.filename.parent / parent.filename.stem / '.csv')
    except Exception:
        pass
        return()


def reformat_mzmine(file):
    data = pd.read_csv(file, sep = ',', header = None, index_col = None)
    data.iloc[0, 0] = 'Compound'
    data.iloc[0, 1] = 'm/z'
    data.iloc[0, 2] = 'Retention time (min)'
    
    xpos = 3
    for elem in data.iloc[0,3:]:
        print(data.iloc[0,xpos])
        data.iloc[0,xpos]=data.iloc[0,xpos].split()[0][:-4]
        xpos += 1
        
    df1 = pd.DataFrame([[np.nan] * len(data.columns)], columns=data.columns)
    data = df1.append(data, ignore_index=True)
    data = df1.append(data, ignore_index=True)
    data.to_csv(file, header = False, index = False) #saves formatted backup for later use


def reformat_msdial(file):
    database = pd.read_csv(file, sep = '\t', header = None, index_col = None) #imports data
    database.iloc[:,3] = database.iloc[:,2]
    database.iloc[:,2] = database.iloc[:,1]
    database.iloc[:,1] = database.iloc[:,3]
    database2 = database.iloc[:,0:3].join(database.iloc[:,32:-10])
    database2.iloc[2,:] = database2.iloc[1,:]
    database2.iloc[3,:] = database2.iloc[1,:]
    database2 = database2.iloc[2:,:]
    database2.iloc[2,:3] = ['Compound', 'm/z', 'Retention time (min)']
    
    database2.to_csv(file.parent / file.stem / '.csv', header = False, index = False) #saves formatted backup for later use This line might break on import of new files...
    database = pd.read_csv(file.parent / file.stem / '.csv', sep = ',', header = [0,1,2], index_col = None) #imports data
    database.iloc[:,0] = database.iloc[:,2].astype(str)+"_"+database.iloc[:,1].astype(str)
    database.to_csv(file.parent / file.stem / '.csv', header = True, index = False) #saves formatted backup for later use This line might break on import of new files...
