"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import numpy as np

class ion():
    def __init__(self, fragparams, pattern):
        self.fragparams = fragparams
        self.pattern = pattern

class fragmentation_db():
    def __init__(self, regex):
        self.regex = regex
        self.ions = {}

def importfrag(fragfile):
    fragmsp = open(fragfile, 'r')
    regex = []
    while True:
        line = fragmsp.readline()
        if (not line) or (':' not in line):
            break
        regex.append(line.split(':')[0])
    fragmsp.close()
    
    fragmsp = open(fragfile, 'r')
    namelist = []
    while True:
        line = fragmsp.readline()
        if not line:
            break
        if 'Name:' in line:
            namelist.append(line.split('(')[1].split(')')[0])
    fragmsp.close()
    
    
    fragmsp = open(fragfile, 'r')
    pairlist = []
    fragparams = {}
    pair = []
    fragdb = fragmentation_db(regex)
    while True:
        line = fragmsp.readline()
        if (not line):
            break
        if 'Name:' in line:
            fragparams = {}
            if line.split('(')[1].split(')')[0] in namelist:
                name = line.split('(')[1].split(')')[0]
                pairlist = []
                while len(line)>5:
                    if ':' in line:
                        fragparams[line.split(':')[0]] = line.split(':')[1]
                    else:
                        pair = line.split('\n')[0].split(' ') #cuts line break an splits at space to seperate mass and abundance
                        pairlist.append([float(pair[0]), float(pair[1])]) #appeds float list
                    line = fragmsp.readline()
                outputarr = np.array(pairlist)
                fragdb.ions[name] = ion(fragparams, outputarr)
    fragmsp.close()
    
    return(fragdb)