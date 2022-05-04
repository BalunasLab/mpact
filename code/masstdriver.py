"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import webbrowser

#def push(description, precursor, fragments):
#webbrowser.open(r"""https://gnps.ucsd.edu/ProteoSAFe/index.jsp#{%22workflow%22:%22SEARCH_SINGLE_SPECTRUM%22,%22precursor_mz%22:%2256.9655%22,%22spectrum_string%22:%2250.798\t6\n51.0098\t58\n53.0178\t1273\n53.5179\t165\n54.0171\t118\n54.1808\t3\n54.4993\t199\n55.0549\t49\n55.9947\t20\n56.0143\t17\n57.0743\t72%22}""")


# version using selenium with nonlogin version of masst
"""
from selenium import webdriver

def push(description, precursor, fragments):
    # Start Chrome Driver
    chromedriver = 'chromedriver'
    
    driver = webdriver.Chrome(chromedriver)
    
    # Open MASST in webdriver
    URL = 'https://masst.ucsd.edu/'
    driver.get(URL)
    
    # Execute JS console commands to push msp data
    #driver.execute_script('console.log($("#description").val(arguments[0]))', description)
    driver.execute_script('console.log($("#precursormz").val(arguments[0]))', precursor)
    driver.execute_script('console.log($("#peaks").val(arguments[0]))', fragments)
"""

