# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:12:43 2021

@author: Xanadu
"""
from indigo import *  
from indigo.renderer import IndigoRenderer
import pandas as pd
import numpy as np


indigo = Indigo()
renderer = IndigoRenderer(indigo)

atlas = pd.read_csv('npatlas.csv', sep = ',', header = [0], index_col = [1])

mass = 445.1126
ppmwindow = 10
hits = atlas.loc[abs(1000000*(atlas['compound_m_plus_h'] - mass)/atlas['compound_m_plus_h']) < ppmwindow,:]

for elem in hits['compound_smiles']:
    m = indigo.loadMolecule(elem)
    renderer.renderToFile(m, elem + '.png')
    

