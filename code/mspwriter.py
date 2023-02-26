# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:19:37 2023

@author: rsamples
"""
import pickle
import os
import io
import pandas as pd


def convert_to_msp(ionfilter_obj, analysis_params):
    """
    Convert ionfilter object to .msp file format.

    Parameters:
    - ionfilter_obj: ionfilter object
        Object containing information about the ions to be extracted
    - analysis_params: analysis_params object
        Object containing information about the location and properties of the input file and output directory

    Returns:
    None

    Behavior:
    - Reads the input csv file and extracts the relevant data
    - Writes a .msp file containing the relevant data from the ionfilter object
    """
    msdata = round(pd.read_csv(analysis_params.filename, sep = ',', header = [0,1,2], index_col = [0]).iloc[:,2:].transpose().mean(), 4)
    ionmerge = ionfilter_obj.merge
    with open(str(analysis_params.outputdir / (analysis_params.filename.stem + '.msp')), 'w') as f:
        keys = list(ionfilter_obj.merge.keys())
        for precursor in keys:
            mass = ionmerge[precursor].target.split('_')[1].strip('m/z').strip('n')
            f.write('Name: Unknown (' + ionmerge[precursor].target + ')\n')  # MSP file requires a name field, but it can be left empty
            f.write('Charge:\n')  # MSP file requires a formula field, but it can be left empty
            f.write('Precursor: ' + mass + '\n')  # MSP file requires a formula field, but it can be left empty
            f.write('Comment: ' + ionmerge[precursor].target + '\n')  # MSP file requires a formula field, but it can be left empty
            numpeaks = 0
            sources = ionmerge[precursor].sources
            for frags in sources:
                numpeaks = len(frags)
            f.write('Num peaks: ' + str(numpeaks) + '\n')  # Number of peaks
            for frags in sources:
                for fragment in frags:
                    f.write(fragment.split('_')[1].strip('m/z').strip('n') + ' ' + str(msdata.loc[fragment]) + '\n')  # Write each source fragment
            f.write('\n')  # MSP file requires a name field, but it can be left empty
            
        f.close()
