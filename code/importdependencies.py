"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import subprocess
import sys
from tkinter import * 
from tkinter import messagebox
import os


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    

installlist = {"epam.indigo":"indigo",
               "UpSetPlot":"upsetplot",
               "squarify":"squarify"}


def checkdep():
    restartflag = False
    installlist = {"epam.indigo":"indigo",
                   "UpSetPlot":"upsetplot",
                   "squarify":"squarify"}
    print('Checking dependencies')
    for package in list(installlist.keys()):
        if installlist[package] in sys.modules:
            print(package + " already installed")
        else:
            restartflag = True
            print('installing ' + package)
            install(package)
    
    if restartflag:
        root = Tk()
        root.geometry("1x1")
        if messagebox.showinfo("Restart", "Dependencies installed, the kernal will restart\n Please restart MPACT"):
            os._exit(00)
        
        root.mainloop()
        
        """
        #code for pyqt version, doesn't work if main window not initialized
        def show_info_messagebox():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
          
            # setting message for Message Box
            msg.setText("Information ")
              
            # setting Message box window title
            msg.setWindowTitle("Information MessageBox")
              
            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
              
            # start the app
            retval = msg.exec_()
                
            show_info_messagebox()
        show_info_messagebox()
        """