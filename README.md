# MPACT

## Installation ##

1. Download and install Anaconda from https://www.anaconda.com/products/individual
2. Download and unzip repository (code>download ZIP) or clone with GitHub Desktop (code>open with GitHub Desktop)

## Startup ##

_Windows_

Double click MPACT shortcut in the main directory (note that nonfatal errors will cause program termination when run in this way and not through an IDE, if you wish to continue in the event of these errors launch through spyder using the Mac steps)

_Mac_

1. Launch spyder through anaconda navigator, or by typing 'spyder' into the anaconda prompt
2. Navigate to code directory in the  main project folder
3. Open main.py (not __main__.py with underscores) in spyder
4. click run button (green arrow in top toolbar)

Full instructions for data processing are included in the MPACT manual.

_Updates in Rev 22.02.26_

- Added data export tab
- Added GNPS peak table filtering functionality (experimental, only tested with FBMN export in MS-DIAL)

_Updates in Rev 22.02.26_

- Added filtering of database hits by kingdom and genus
- Dependency check script spawns a window if any dependencies were installed informing user the kernal will restart.
- Bugfixes in group set interactions, and bruker data import

_Updates in Rev 22.02.19_

- Added support for Bruker Metaboscape peak lists
- Added support for MS-DIAL MSP files
- Added MSP file writer to export in-source fragmentation patterns
- Reduced lag when selecting features
- Added multithreading when generating feature abundance plots
- Fixed bug that resulted in feature highlights not being visible in data reanalysis
- Fixed issue preventing samples/injections from being selected and highlighted in NMDS plots
- Database hit images viewed are saved as images in a folder to eliminate rerendering
