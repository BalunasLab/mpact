# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:45:17 2022

@author: rsamples
"""

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

installlist = {"epam.indigo":"indigo",
               "UpSetPlot":"upsetplot",
               "squarify":"squarify"}

def checkdep():
    installlist = {"epam.indigo":"indigo",
                   "UpSetPlot":"upsetplot",
                   "squarify":"squarify"}
    print('Checking dependencies')
    for package in list(installlist.keys()):
        if installlist[package] in sys.modules:
            print(package + " already installed")
        else:
            print('installing ' + package)
            install(package)