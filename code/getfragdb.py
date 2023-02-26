
import numpy as np

class ion():
    """
    A class representing a ion with associated fragmentation data.
    
    Attributes:
    -----------
    fragparams: dict
        A dictionary of parameters for the ion.
    pattern: np.ndarray
        A numpy array representing the ion's pattern.
    """
    
    def __init__(self, fragparams, pattern):
        self.fragparams = fragparams
        self.pattern = pattern

class fragmentation_db():
    """
    A class representing a database of fragmentation ions.
    
    Attributes:
    -----------
    regex: list
        A list of regular expressions for the database.
    ions: dict
        A dictionary of ions in the database.
    """
    
    def __init__(self, regex):
        self.regex = regex
        self.ions = {}

def importfrag_v1(fragfile):
    """
    Imports a fragmentation database from a Progenesis-style MSP file.
    
    Parameters:
    -----------
    fragfile: str
        The path to the MSP file.
    
    Returns:
    --------
    fragmentation_db
        A database of fragmentation ions.
    """
    
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

def importfrag_v2(fragfile):
    """
    Imports a fragmentation database from an MS-DIAL-style MSP file.
    
    Parameters:
    -----------
    fragfile: str
        The path to the MSP file.
    
    Returns:
    --------
    fragmentation_db
        A database of fragmentation ions.
    """
    fragmsp = open(fragfile, 'r')
    regex = []
    while True:
        line = fragmsp.readline()
        
        if (not line) or (':' not in line):
            break
        regex.append(line.split(':')[0])
    fragmsp.close()
    
    fragmsp = open(fragfile, 'r')
    fragparams = {}
    fragdb = fragmentation_db(regex)
    while True:
        line = fragmsp.readline()
    
        if not line:
            break
        pairlist = []
        while len(line)>5:
            while ':' in line:
                fragparams[line.split(':')[0]] = line.split(':')[1].strip()
                line = fragmsp.readline()
            line = fragmsp.readline()
            
            while ':' not in line and len(line)>5:
                if not line or 'NAME:' in line.upper():
                    break
                pair = line.split()
                pairlist.append([float(pair[0]), float(pair[1])])
                line = fragmsp.readline()
        outputarr = np.array(pairlist)
        name = str(round(float(fragparams['RETENTIONTIME']),3))  + '_' + fragparams['PRECURSORMZ']
        fragdb.ions[name] = ion(fragparams, outputarr)
    fragmsp.close()

    return(fragdb)

def importfrag(fragfile):
    """
    Imports a fragmentation database from an MSP file, detecting the file type automatically.
    
    Parameters:
    -----------
    fragfile: str
        The path to the MSP file.
    
    Returns:
    --------
    fragmentation_db
        A database of fragmentation ions.
    """
    
    fragmsp = open(fragfile, 'r')
    has_parentheses = False
    while True:
        line = fragmsp.readline()
        print(has_parentheses)
        print(line)

        if not line:
            break
        if 'NAME:' in line.upper() and '(' in line and ')' in line:
            has_parentheses = True
            break
    fragmsp.close()
    
    if has_parentheses:
        print('Progenesis MSP file Detected')
        return importfrag_v1(fragfile)
    else:
        print('MS-DIAL MSP file Detected')
        return importfrag_v2(fragfile)

