"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import re

import sys
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import time
import string

import platform
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QFileDialog, QListWidgetItem, QColorDialog
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import QBrush, QColor, QIcon, QPalette, QPainter, QPixmap
from pathlib import Path

# GUI FILE
from ui_main import Ui_MainWindow
import ui_plotparam
import ui_featureinfo

# IMPORT FUNCTIONS AND RESOURCES
from ui_functions import *
import files

from MSFaST import run_MSFaST, analysis_parameters
from plotting import plot_abund, show_spectrum, show_featureplt, plot_heatmap, plot_mzrt, plot_samplecorr, kendrick, plot_volcano, plot_fc3d, plot_dendrogram, plot_PCA, prev_cv, gen_upsetplt, gen_treemap
import getfragdb

from indigo import Indigo
from indigo.renderer import IndigoRenderer
indigo = Indigo()
renderer = IndigoRenderer(indigo)
import os

import pickle


import pathlib
if sys.platform == 'win32':
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
else:
    temp = pathlib.WindowsPath
    pathlib.WindowsPath = pathlib.PosixPath
    

'''
#need to make sure rel vs absolute is stored, and that merge checkbox connected, add to load filey
Check if low_memory=False increases ram usage for average grps?

-add bypass for plots based on checkmark. possibly use if check: ... else: button.hide() then pass

- distribution of CVs on bottom of cvplt?
- add pca option and allow visualization of key features on multivar plt?

#TODO#
#Easy/high priority
- in source spectra
- do overall data quality score, AUC
- standardize method and class names
- database management, options
- fix up analysisinfo file output

#Medium priority
- mzmine msp file import
- add other ordination options
- add custom keyword arguments for each plot to make calling them easier
- add more conditionals so if one plot fails it doesn't kill everything else
- add runcheck before searching when switching to search tab
- Figure out way to have only active plot be updated and then to update others
    when plot is switched
- change treewidget in search tab to treeview for better search, add filter options
- make it so groups can be reordered
- make it so iondict and msdata are saved as a parent object so they dont need to
    be reopened each time a heatmap feature is scrolled. This may actually not
    be a good idea depending on ram demands
- make goto buttons just one class and lambda an index for the stacked widgets
    when connecting!

#low priority/long term
- Switch to MVC format for groupsets
- maybe have a comparison mode for many different strains with and without elicitor
- specificity/sensitivity plot
- other statistical models
- refactor the filtereddfs and groupset code. everything should probably
    be filtered from the main file in the analysis by referencing the groups
    column in iondict
    ~best way to do this may be to simplify the query/groupset flow to only have
    one object, and then to generate a list of ions that pass this filter in the
    object. That or add a color column to the iondict file
    ~refactor to run filtering based of a list of filters instead of several 
    conditionals each time OR do it so that the appropriate columns are still 
    generated each time if filtering is off but they are always true
'''

class NumericalTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __lt__(self, other):
        column = self.treeWidget().sortColumn() # the second column
        try:
            return float(self.text(column)) < float(other.text(column))
        except ValueError: # fallback to alphabetical sorting if the text is not a number
            return super().__lt__(other)

class query:
    """
    Defines conditions (group presence/absence) to plot feature in a colour
    """
    def __init__(self):
        self.name = ''
        self.src = ''  # or groups, feature can be in
        self.incl = ''  # and groups, feature must be in
        self.excl = ''  # not groups, feature must not be in
        self.colour = '#000000'


fullruntime = 0


def start_functime():
    """
    Used to calculate runtime
    """
    global initfunctime
    initfunctime = time.time()


def stop_functime(text):
    """
    Prints runtime for step and increments global runtime
    """
    final = time.time()
    interval = final - initfunctime
    global fullruntime
    fullruntime = fullruntime + interval
    print(text)
    print(interval)
    print('')
    start_functime()


def reset_runtime():
    """
    Resets for new analysis
    """
    global fullruntime
    fullruntime = 0
        
    
#UI WINDOWS#
class ftrdialog(QMainWindow): #dialog window for feature level data (spec, abund, hits)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_featureinfo.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.sizegrip = QSizeGrip(self.ui.frame_grip_corner)
        self.ui.frame_grip_corner.setStyleSheet("background: transparent; background-image: url(:/resources/icons/24x24/resize.png); background-position: center; background-repeat: no-repeat;" )
        self.sizegrip.setToolTip("Resize Window")
        
        # MOVE WINDOW
        def moveWindow(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos2)
                self.dragPos2 = event.globalPos()
                event.accept()
        
        self.ui.label_title_bar_top.mouseMoveEvent = moveWindow 
        
    def mousePressEvent(self, event):
        self.dragPos2 = event.globalPos()
        
class dialog(QMainWindow): #plot configuration dialog
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_plotparam.Ui_MainWindow()
        self.ui.setupUi(self)
        
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos2)
                self.dragPos2 = event.globalPos()
                event.accept()
        
        self.ui.label_title_bar_top.mouseMoveEvent = moveWindow
        
    def mousePressEvent(self, event):
        self.dragPos2 = event.globalPos()
        
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)  # set always on top flag, makes window disappear
        self.show() # makes window reappear, but it's ALWAYS on top
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint) # clear always on top flag, makes window disappear
        #self.show() # makes window reappear, acts like normal window now (on top now but can be underneath if you raise another window)
        
        self.ui.setupUi(self)
        self.ui.label_credits.setText('Rev 23.02.26')
                
        #initialize other dialog windows
        self.dialog = dialog()
        self.ftrdialog = ftrdialog()
        self.ftrdialog.ui.btn_masst.hide()

        #set defaults
        self.recentdir = '..'
        self.savedata = {}
        self.pickedfeature = ''
        self.highlightcol = 'yellow'
        self.dbsearchdone = False
        self.selset = -1 #selected groupset index, refactor with MVC design
        self.querys = [] #dictionary of the query/groupset objects
        self.groups = [] #biological groups in the dataset
        self.filename = Path.cwd()
        self.extractmetadatafilename = Path.cwd()
        self.samplelistfilename = Path.cwd()
        self.ui.label_status.setText('') #running/idle status label
        self.analysisrun = False
        self.ui.combo_maxisoshift.setCurrentIndex(3)
        self.outputdir = ''
        self.fragfilename = ''
        self.colourdic = {} #dictionary of available colours
        #self.atlas = pd.read_csv('npatlas.csv', sep = ',', header = [0], index_col = [1])
        #self.atlas = pd.read_csv('pyranodb.csv', sep = ',', header = [0], index_col = [1])

        

        
        #initialize figure element dictionaries, can call with self.currplot as key
        self.fig = {}
        self.canvas = {}
        self.pltlayout = {}
        self.toolbar = {}
        self.ax = {}
        self.highlight = {}
                
        self.ui.btn_run.clicked.connect(self.run_analysis)

        def moveWindow(event):
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.label_title_bar_top.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
        self.show()


    #---Methods---
    def exportgnps(self):  #move processing function to a different method                                                                        "*.txt")
            # Load the first four rows (header) of the first file
            header = pd.read_csv(self.gnpsfilename, nrows=4, keep_default_na=False, header=None,sep='\t')

            # Ensure header has the same columns as df1
            header.columns = range(header.shape[1])

            # Load first file skipping first four rows
            df1 = pd.read_csv(self.gnpsfilename, skiprows=4, header=None,sep='\t')

            # Creating 'Compound' column in df1 by combining 'Average Rt(min)' and 'Average Mz'
            df1['Compound'] = df1.iloc[:,1].astype(str) + '_' + df1.iloc[:,2].astype(str)

            # Load second file with three header rows
            df2 = pd.read_csv(self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'), header=[0,1,2])

            # Convert 'Compound' column in df2 to set for faster lookup
            compounds = set(df2['Unnamed: 0_level_0', 'Unnamed: 0_level_1','Compound'])

            # Filter df1 based on 'Compound' column
            df1_filtered = df1[df1['Compound'].isin(compounds)]

            # Remove 'Compound' column from df1_filtered
            df1_filtered = df1_filtered.drop('Compound', axis=1)
            
            # Combine header and filtered DataFrame
            df_final = pd.concat([header, df1_filtered], ignore_index=True).fillna('null')

            df_final.to_csv(self.analysis_paramsgui.outputdir / (self.gnpsfilename.stem + '_filtered.txt'),sep='\t', index=False, header = False)
            self.ui.label_status.setText('Filtered GNPS peak table exported to output directory')
    
    def error(self, message):
        self.ui.label_status.setText(message)
        self.ui.label_status.setStyleSheet('color: rgb(150,0,0);')
    
    def getgroups(self):
        """
        Get biological groups on input of all input files, fills comboboxes with these.
        """
        extractmetadata = pd.read_csv(self.extractmetadatafilename, sep=',', header=[0], index_col=None)
        samplelist = pd.read_csv(self.samplelistfilename, sep=',', header=[0], index_col=None)
    
        try:
            combinedmetadata = extractmetadata.set_index('Sample_Code').join(samplelist.set_index('Sample_Code')) \
                                                    .reset_index().set_index('Injection')
        except Exception:
            self.error('Data read failure: Check input files')
            return
    
        msdata = pd.read_csv(self.filename, sep=',', header=None, index_col=[0, 1, 2])
        groups = []
    
        for elem in msdata.iloc[2]:
            biolgroup = combinedmetadata.loc[elem, 'Biological_Group']
            if biolgroup not in groups:
                groups.append(combinedmetadata.loc[elem, 'Biological_Group'])
    
        self.groups = groups
    
        # Set experimental and control grp defaults in ui
        self.ui.combo_blankfil_name.clear()
        self.ui.combo_blankfil_name.addItems(self.groups)
        self.ui.combo_expgrp.clear()
        self.ui.combo_expgrp.addItems(self.groups)
        self.ui.combo_ctrgrp.clear()
        self.ui.combo_ctrgrp.addItems(self.groups)
            
        # Set experimental and control group defaults in ui
        pos = 0
        expset = False
        for group in self.groups:
            if 'blank' in group.lower():
                self.ui.combo_blankfil_name.setCurrentIndex(pos)
            else:
                if expset:
                    self.ui.combo_ctrgrp.setCurrentIndex(pos)
                else:
                    self.ui.combo_expgrp.setCurrentIndex(pos)
                    expset = True
            pos += 1
    
        
    def fulldbsearch(self):
        """
        Run a full compound database search. Filter the database matches within a specified mass window.
        Concatenate the hits and sort them by parts-per-million (ppm).
        """
        self.hitdb = {}
        iondict = pd.read_csv(self.analysis_paramsgui.outputdir / 'iondict.csv', sep=',', header=[0], index_col=[0])
        iondict['hits'] = ''
        msdata = pd.read_csv(self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'), sep=',', header=[2], index_col=None).iloc[:, :3]
    
        for _, mrow in msdata.iterrows():
            # Iterates over iondict, filters DB matches within window.
            # Repeats for adducts, uses length of concat DF for feature hits
            mass = mrow['m/z']
            ppmwindow = self.analysis_paramsgui.ppmthresh
            hits_h = self.atlas[abs(1000000 * (self.atlas['compound_m_plus_h'] - mass) / self.atlas['compound_m_plus_h']) < ppmwindow]
            hits_h['ppm'] = abs(1000000 * (hits_h['compound_m_plus_h'] - mass) / hits_h['compound_m_plus_h'])
            hits_na = self.atlas[abs(1000000 * (self.atlas['compound_m_plus_na'] - mass) / self.atlas['compound_m_plus_na']) < ppmwindow]
            hits_na['ppm'] = abs(1000000 * (hits_na['compound_m_plus_na'] - mass) / hits_na['compound_m_plus_na'])
            hits = pd.concat([hits_h, hits_na])
            hits = hits.sort_values(by=['ppm'])
            self.hitdb[mrow['Compound']] = hits
            iondict.loc[mrow['Compound'], 'hits'] = hits.shape[0]
    
        iondict.to_csv(self.analysis_paramsgui.outputdir / 'iondict.csv', header=True, index=True)

        
    def fillfttree(self):
        # Fill feature tree with database hits
        iondict = pd.read_csv(self.analysis_paramsgui.outputdir / 'iondict.csv', sep=',', header=[0], index_col=None)
        iondict = iondict[iondict['hits'] >= 0]
        self.ui.treeWidget.setSortingEnabled(True)
    
        itemdict = {}
        self.ui.treeWidget.clear()
        for i, row in iondict.iterrows():
            item = NumericalTreeWidgetItem([row['Compound'], str(round(row['m/z'], 4)), str(round(row['Retention time (min)'], 3)), str(int(row['max'])), str(row['groups']), str(row['groups']), str(round(row['fc'], 2)), str(int(row['hits']))])
            itemdict[i] = item
            self.ui.treeWidget.addTopLevelItem(item)
    
        def onItemClicked():
            # Rename to onItemClicked
            item = self.ui.treeWidget.selectedItems()[0]
            pickedfeature = item.text(0)
            self.highlight_feature(pickedfeature)  # Highlights the selected feature
    
        self.ui.treeWidget.itemSelectionChanged.connect(onItemClicked)
                

                                     
    def runsearch(self, mass): # refactor if I can save a database of hits
        #possibly make a third common method used in both dbsearch and this method
        """
        Runs a search for a mass and displays the database hits in the feature tree dialog.
        
        Args:
            mass (float): The mass to search for.
        
        Returns:
            None.
        """
        ppmwindow = self.analysis_paramsgui.ppmthresh
        hits_h = self.atlas[abs(1000000*(self.atlas['compound_m_plus_h'] - mass)/self.atlas['compound_m_plus_h']) < ppmwindow]
        hits_h['ppm'] = abs(1000000*(hits_h['compound_m_plus_h'] - mass)/hits_h['compound_m_plus_h'])
        hits_na = self.atlas[abs(1000000*(self.atlas['compound_m_plus_na'] - mass)/self.atlas['compound_m_plus_na']) < ppmwindow]
        hits_na['ppm'] = abs(1000000*(hits_na['compound_m_plus_na'] - mass)/hits_na['compound_m_plus_na'])
        hits = pd.concat([hits_h, hits_na])
        hits = hits.sort_values(by=['ppm'])
        
        x=0 #rename this variable
        itemdict = {}
        smilesdict = {}
        self.ftrdialog.ui.treeWidget.clear()
        for index, row in hits.iterrows():
            itemdict[x] = QtWidgets.QTreeWidgetItem( [row['compound_names'], row['compound_molecular_formula'], str(row['compound_accurate_mass']), str(row['ppm']), (str(row['genus'] + ' ' + row['origin_species'])), row['compound_smiles']])
            self.ftrdialog.ui.treeWidget.addTopLevelItem(itemdict[x])
            x = x + 1
        
        def onItemClicked(): #show structure of selected match
        
            def clean_ascii(text):
                printable = set(string.printable)
                ascii_chars = filter(lambda x: x in printable, text)
                return ''.join(ascii_chars)
        
                
            if len(self.ftrdialog.ui.treeWidget.selectedItems()) > 0:
                item = self.ftrdialog.ui.treeWidget.selectedItems()[0]
                cmpd =  clean_ascii(item.text(0))
                cmpd = re.sub(r'\/<>.*{}\|', ' ', cmpd)

                if os.path.isfile('compoundimages/' + (cmpd + '.png')):
                    pixmap = QPixmap('compoundimages/' + (cmpd + '.png'))
                else:
                    m = indigo.loadMolecule(item.text(5))
                    indigo.setOption('render-image-size', '400,400')
                    renderer.renderToFile(m, 'compoundimages/' + (cmpd + '.png'))
                    pixmap = QPixmap('compoundimages/' + (cmpd + '.png'))
                
                pixmap2 = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
                self.ftrdialog.ui.label.setPixmap(pixmap2)
        
        self.ftrdialog.ui.treeWidget.itemSelectionChanged.connect(onItemClicked)
        if len(hits.index) == 0:
            pixmap = QPixmap('blank.png')
            pixmap2 = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
            self.ftrdialog.ui.label.setPixmap(pixmap2)
        else:
            self.ftrdialog.ui.treeWidget.setCurrentItem(itemdict[0])
                
    def highlight_feature(self, newfeature):
        """
        Highlights the selected feature in all plots.

        Args:
            newfeature (str): The name of the new feature to highlight.
        
        Returns:
            None.
        """
        # Deselect the highlighted feature if clicked twice
        if newfeature == self.pickedfeature and self.highlightcol != (0, 0, 0, 0):
            self.highlightcol = (0, 0, 0, 0)
        else:
            self.highlightcol = 'yellow'
            
        # Highlight the selected feature in all plots
        for plot in self.highlight:
            self.highlight[plot].set_color(self.highlightcol)
            
        # Set the selected feature as the picked feature
        self.pickedfeature = newfeature
        
        # Read iondict file to get ion data
        iondict = pd.read_csv(self.analysis_paramsgui.outputdir / 'iondict.csv',
                              sep=',', header=[0], index_col=[0])
        
        # Update volcano plot with the selected feature
        if self.analysis_paramsgui.Volcanoplt:
            self.highlight['volcano'].set_data(iondict.loc[self.pickedfeature, 'logfc'],
                                                iondict.loc[self.pickedfeature, '-logq'])
            self.canvas['volcano'].draw_idle()
        
        # Update MZRT plot with the selected feature
        if self.analysis_paramsgui.MZRTplt:
            self.highlight['mzrt'].set_data(iondict.loc[self.pickedfeature, 'Retention time (min)'],
                                            iondict.loc[self.pickedfeature, 'm/z'])
            self.canvas['mzrt'].draw_idle()
        
        # Update KMD plot with the selected feature
        if self.analysis_paramsgui.KMD:
            self.highlight['kmd'].set_data(iondict.loc[self.pickedfeature, 'm/z'],
                                           iondict.loc[self.pickedfeature, 'kmd'])
            self.canvas['kmd'].draw_idle()
        
        # Update feature plot with the selected feature
        self.highlight['featureplt'].set_data(iondict.loc[self.pickedfeature, 'Retention time (min)'],
                                               iondict.loc[self.pickedfeature, 'm/z'])
        self.canvas['featureplt'].draw_idle()
        
        msdata = pd.read_csv(self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'),
                              sep=',', header=[2], index_col=[0])
        
        # Set heatmap highlight based on view
        self.heatind = self.cmind.index(msdata.index.to_list().index(self.pickedfeature))
        xlim = int(self.canvas['heatmap'].figure.axes[2].get_xlim()[1])
        self.highlight['heatmap'].set_data([0, xlim, xlim, 0, 0], [self.heatind, self.heatind, self.heatind+1, self.heatind+1, self.heatind])
        self.canvas['heatmap'].draw_idle()
        
        # Run search when feature is selected
        if self.ftrdialog.ui.stackedWidget.currentIndex() == 0 and not self.ftrdialog.isHidden():
            self.runsearch(iondict.loc[self.pickedfeature, 'm/z'])
        
        # Reset spec if fragfilename exists and update abundplt
        if self.fragfilename != '':
            self.spec.reset(self.fragdb.ions[self.pickedfeature].pattern)
        if self.ftrdialog.ui.stackedWidget.currentIndex() == 2 and not self.ftrdialog.isHidden():
            self.abundplt.reset()

     # Move heatmap selection up or down with W/S key press
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.mv_heatmap(-1)
        elif event.key() == QtCore.Qt.Key_S:
            self.mv_heatmap(1)
    
    def mv_heatmap(self, shift):
        """
        Moves heatmap selection up or down by a given shift value.
        
        Args:
            shift (int): The value to shift the heatmap selection by.
        
        Returns:
            None.
        """
        if self.ui.stackedWidget_plot.currentIndex() != 8 or self.ui.stackedWidget.currentIndex() != 3:
            return
    
        iondict = pd.read_csv(self.analysis_paramsgui.outputdir / 'iondict.csv', sep=',', header=[0], index_col=[0])
        msdata = pd.read_csv(self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'), sep=',', header=[2], index_col=[0]).iloc[:, 2:]
        index = self.cmind[self.heatind + shift]
        name = msdata.index.tolist()[index]
    
        self.ui.lbl_featurename.setText('Compound: ' + name)
        self.ui.lbl_featurert.setText('Retention time: ' + str(iondict.loc[name, 'Retention time (min)']))
        self.ui.lbl_featuremz.setText('m/z: ' + str(iondict.loc[name, 'm/z']))
        self.highlight_feature(name)
     
    
    def read_save(self, savefile):
        """Reads a saved analysis session from a pickle file.

        Args:
            savefile (Path): The path to the saved session file.
        """
        with open(savefile, 'rb') as read_pi:
            self.savedata = pickle.load(read_pi)
    
        # Assign the analysis parameters
        self.analysis_paramsgui = self.savedata['parameters']
            
        # Set output dir to save file directory, make rawdata folder
        self.analysis_paramsgui.outputdir = Path(savefile).parent
        Path(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata').mkdir(parents=True, exist_ok=True)
            
        # Write raw files from save file
        self.savedata['peaktable'].to_csv(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / self.analysis_paramsgui.filename.name, header=False, index=False)
        self.savedata['samplelist'].to_csv(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / self.analysis_paramsgui.samplelistfilename.name, header=False, index=False)
        self.savedata['extractmetadata'].to_csv(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / self.analysis_paramsgui.extractmetadatafilename.name, header=False, index=False)
        
        # Write frag file if it exists
        if self.analysis_paramsgui.fragfilename:
            fragmsp = open(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / self.analysis_paramsgui.fragfilename.name, 'w')     
            fragmsp.write(self.savedata['fragdb'])
            fragmsp.close()
            
        # Assign file names and output directory
        self.outputdir = self.analysis_paramsgui.outputdir
        self.samplelistfilename = self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / self.analysis_paramsgui.samplelistfilename.name
        self.extractmetadatafilename = self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / self.analysis_paramsgui.extractmetadatafilename.name
        
        # Assign frag file name if it exists
        if self.analysis_paramsgui.fragfilename:
            self.fragfilename = self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / Path(self.analysis_paramsgui.fragfilename).name
        
        self.filename = self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'rawdata' / self.analysis_paramsgui.filename.name
    
        # Get groups and update querys
        self.getgroups()
        self.querys = self.analysis_paramsgui.queries
        UIFunctions.updatesets(self)
        
        
    def write_save(self):
        """Writes the current analysis session to a pickle file.
        """
        self.analysis_paramsgui.queries = self.querys # WRITES QUERY DB FOR GROUPSETS IN ANALYSISPARAMETERS, WILL NEED TO CHANGE WHEN MVC IMPLEMENTED
        file_pi = open(self.analysis_paramsgui.outputdir/(self.analysis_paramsgui.filename.stem + '.mpct'), 'wb')
        self.savedata['parameters'] = self.analysis_paramsgui
        self.savedata['peaktable'] = pd.read_csv(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.name, sep = ',', header = None, index_col = None)
        self.savedata['samplelist'] = pd.read_csv(self.samplelistfilename, sep = ',', header = None, index_col = None)
        self.savedata['extractmetadata'] = pd.read_csv(self.extractmetadatafilename , sep = ',', header = None, index_col = None)
        if self.analysis_paramsgui.fragfilename != '':
            fragmsp = open(self.analysis_paramsgui.fragfilename, 'r')     
            self.savedata['fragdb'] = fragmsp.read()
            fragmsp.close()
        else:
            self.savedata['fragdb'] = 'None'
        pickle.dump(self.savedata, file_pi)
        file_pi.close()
    
    def run_analysis(self):
        self.dbsearchdone = False
        start_functime()
        self.enumerate_inputs()
        print('')
        stop_functime('inputs obtained')
        
        # Insert working signal here, will likely need multithreading
        run_MSFaST(self)
        print('')
        stop_functime('calculations complete')
        
        gen_treemap(self)  # move back to end
        stop_functime('treemap complete')
        
        # Used for point opacity based on abundance colouring
        iondict = pd.read_csv(self.analysis_paramsgui.outputdir / 'iondict.csv', sep=',', header=[0], index_col=None)
        self.analysis_paramsgui.maxval = iondict['logmax'].max()
        
        if self.analysisrun:
            self.regenerateplts()
        else:
            self.ftplt = show_featureplt(self, 'featureplt', self.ui.frame_featureplt, self.analysis_paramsgui.outputdir / 'iondict.csv', '', '')
            stop_functime('ftplt complete')
        
            self.dend = plot_dendrogram(self, 'dend', self.ui.frame_dend, self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'), '', '')
            stop_functime('dendrogram complete')
        
            if self.analysis_paramsgui.PCA:
                self.pca = plot_PCA(self, 'pca', self.ui.frame_pca, self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'), '', '')
                stop_functime('nmds complete')
        
            if self.analysis_paramsgui.FC3Dplt:
                self.fc3d = plot_fc3d(self, 'fc3d', self.ui.frame_fc3d,  self.analysis_paramsgui.outputdir / 'iondict.csv', self.filtereddfs, self.groupsets) 
                stop_functime('fc3d complete')
        
            if self.analysis_paramsgui.KMD:
                self.kmd = kendrick(self, 'kmd', self.ui.frame_kmd, self.analysis_paramsgui.outputdir / 'iondict.csv', self.filtereddfs, self.groupsets)
                stop_functime('kmd complete')
        
            if self.analysis_paramsgui.MZRTplt:
                self.mzrt = plot_mzrt(self, 'mzrt', self.ui.frame_mzrt, self.analysis_paramsgui.outputdir / 'iondict.csv', self.filtereddfs, self.groupsets)
                stop_functime('mzrt complete')
        
            if self.analysis_paramsgui.Volcanoplt:
                self.volcano = plot_volcano(self, 'volcano', self.ui.frame_volcano, self.analysis_paramsgui.outputdir / 'iondict.csv', self.filtereddfs, self.groupsets)
                stop_functime('volcano complete')
        
            self.heatmap = plot_heatmap(self,  'heatmap', self.ui.frame_heatmap, self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'))
            stop_functime('heatmap complete')
        
            self.abundplt = plot_abund(self, 'abund')
        
            if self.fragfilename != '':
                self.spec = show_spectrum(self, 'spec')
        
            if self.analysis_paramsgui.CVfil:
                self.prevcv = prev_cv(self, 'cvplt', self.ui.frame_cvplt, 'none', 'none', 'none')
                stop_functime('cvplt complete')
        
            self.samplecorr = plot_samplecorr(self, 'samplecorr', self.ui.frame_samplecorr, self.analysis_paramsgui.outputdir / 'iondict.csv', self.filtereddfs, self.groupsets)
            stop_functime('samplecorr complete')
        
        self.analysisrun = True
        
        #text = open(self.analysis_paramsgui.outputdir / 'analysisinfo.txt').read() #writes output text to report tab
        #self.ui.textBrowser_info.setPlainText(text)
    
    

        # Writes filtering statistics in data review summary
        msdata_unformatted = pd.read_csv(self.analysis_paramsgui.filename, sep=',', header=[0, 1, 2], index_col=[0, 1, 2])
        msdata_formatted = pd.read_csv(self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_formatted.csv'), sep=',', header=[0, 1, 2], index_col=[0, 1, 2])
        msdata_filtered = pd.read_csv(self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv'), sep=',', header=[0, 1, 2], index_col=[0, 1, 2])
        #test = open('testionfilters.pkl', 'wb') # this exports ionfilters as a pickle for debuging
        #pickle.dump(self.ionfilters, test)
        
        text = ''
        if self.analysis_paramsgui.relfil:
            text += 'Features failing peak correction filtering: ' + str(len(self.ionfilters['relfil'].ions)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.ionfilters['relfil'].ions) / len(msdata_unformatted.index), 2)) + '%\n'
        if self.analysis_paramsgui.blnkfltr:
            text += 'Features failing blank filtering: ' + str(len(self.groupionlists[self.analysis_paramsgui.blnkgrp])) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.groupionlists[self.analysis_paramsgui.blnkgrp]) / len(msdata_unformatted.index), 2)) + '%\n'
        if self.analysis_paramsgui.decon:
            text += 'Features in-source ion filtering: ' + str(len(self.ionfilters['insource'].ions)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.ionfilters['insource'].ions) / len(msdata_unformatted.index), 2)) + '%\n'
        if self.analysis_paramsgui.CVfil:
            text += 'Features failing CV filtering: ' + str(len(self.ionfilters['cv'].ions)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(self.ionfilters['cv'].ions) / len(msdata_unformatted.index), 2)) + '%\n'
        text += 'Features failing any filters: ' + str(len(msdata_unformatted.index) - len(msdata_filtered.index)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * (len(msdata_unformatted.index) - len(msdata_filtered.index)) / len(msdata_unformatted.index), 2)) + '%\n'
        text += 'Features passing all filters: ' + str(len(msdata_filtered.index)) + '/' + str(len(msdata_unformatted.index)) + ' ' + str(round(100 * len(msdata_filtered.index) / len(msdata_unformatted.index), 2)) + '%\n'
        
        self.ui.textBrowser_mp_prev.setPlainText(text)
        
        # Imports msp fragment database
        if self.fragfilename != '':
            self.fragdb = getfragdb.importfrag(self.analysis_paramsgui.fragfilename)
            self.ftrdialog.ui.btn_spectrum.show()
        else:
            self.fragdb = 'None'
            self.ftrdialog.ui.btn_spectrum.hide()
        
        # Runs DB search only if tab is active
        if self.ui.stackedWidget.currentIndex() == 5:
            self.fulldbsearch()
            self.fillfttree()
            self.dbsearchdone = True
        
        gen_upsetplt(self)
        stop_functime('upsetplt complete')
        self.ui.label_status.setText('Analysis Complete')
        stop_functime('analysis complete')
        print('')
        print('full runtime:' + str(fullruntime))
        print('')
        print('')
        reset_runtime()
        
        
        self.write_save()
        
    def enumerate_inputs(self):
        self.analysis_paramsgui = analysis_parameters()
        if self.ui.checkBox_blankfilter.isChecked():
            self.analysis_paramsgui.blnkgrp = str(self.ui.combo_blankfil_name.currentText())
        else:
            self.analysis_paramsgui.blnkgrp = ''
        self.analysis_paramsgui.blnkfltr = self.ui.checkBox_blankfilter.isChecked()

        if len(self.querys) == 0:
            if self.analysis_paramsgui.blnkfltr:
                UIFunctions.addgroup(self, 'Features not in blanks')
                self.querys[0].src = self.querys[0].excl
                self.querys[0].src.remove(self.analysis_paramsgui.blnkgrp)
                self.querys[0].excl = [self.analysis_paramsgui.blnkgrp]
            else:
                UIFunctions.addgroup(self, 'All features')
                self.querys[0].src = self.querys[0].excl
                self.querys[0].excl = []
            UIFunctions.updategroups(self)
        else:
            self.selset = self.ui.listWidget_pltgrps.currentRow()
            UIFunctions.writegroups(self)
            UIFunctions.updategroups(self)
        
        self.analysis_paramsgui.kingdom = self.ui.combo_kingdom.currentText()
        self.analysis_paramsgui.genus = str(self.ui.lineEdit_genus.text())
        self.atlas = pd.read_csv('npatlas.csv', sep = ',', header = [0], index_col = [1])
        if len(self.analysis_paramsgui.kingdom) > 3:
            self.atlas = self.atlas[self.atlas['origin_type'] == self.analysis_paramsgui.kingdom]
        if len(self.analysis_paramsgui.genus) > 3:
            self.atlas = self.atlas[self.atlas['genus'] == self.analysis_paramsgui.genus]

        
        self.analysis_paramsgui.graphfilters = ''
        if self.ui.checkBox_cv.isChecked():
            self.analysis_paramsgui.graphfilters += 'cv '
        if self.ui.checkBox_mp.isChecked():
            self.analysis_paramsgui.graphfilters += 'rel '
        if self.ui.checkBox_decon.isChecked():
            self.analysis_paramsgui.graphfilters += 'insource'
            self.analysis_paramsgui.deconthresh = float(self.ui.lineEdit_insourcethresh.text())
        
        

        
        tempquerydic = {}
        for pos in range(len(self.querys)):
            tempquery = query()
            tempquery.colour = str(self.querys[pos].colour)
            tempquery.name = self.querys[pos].name
            tempquery.excl = ' '.join(self.querys[pos].excl)
            tempquery.incl = ' '.join(self.querys[pos].incl)
            tempquery.src = ' '.join(self.querys[pos].src)
            tempquerydic[pos] = tempquery
            
        querydict = {}
        for elem in tempquerydic:
            tempquerydic[elem].excl += ' ' + self.analysis_paramsgui.graphfilters
            queryname = tempquerydic[elem].src + ' +' + tempquerydic[elem].incl + ' -' + tempquerydic[elem].excl + ' c=' + tempquerydic[elem].colour + ' n=' + tempquerydic[elem].name
            tempquerydic[elem].src = tempquerydic[elem].src.split()
            tempquerydic[elem].incl = tempquerydic[elem].incl.split()
            tempquerydic[elem].excl = tempquerydic[elem].excl.split()
            querydict[queryname] = tempquerydic[elem]
        
        self.analysis_paramsgui.querydict = querydict
        self.analysis_paramsgui.querylist = list(querydict.keys())
        
        # Set analysis parameters
        self.analysis_paramsgui.filename = self.filename
        self.analysis_paramsgui.samplelistfilename = self.samplelistfilename
        self.analysis_paramsgui.extractmetadatafilename = self.extractmetadatafilename 
        if self.outputdir == '':
            self.outputdir = (Path(self.analysis_paramsgui.filename).parent)
        self.analysis_paramsgui.outputdir = self.outputdir
        self.analysis_paramsgui.fragfilename = self.fragfilename
        Path(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem).mkdir(parents=True, exist_ok=True)
        Path(self.analysis_paramsgui.outputdir / self.analysis_paramsgui.filename.stem / 'plots').mkdir(parents=True, exist_ok=True)
        self.analysis_paramsgui.outputdir /= self.analysis_paramsgui.filename.stem
    
        self.analysis_paramsgui.statstgrps = [str(self.ui.combo_expgrp.currentText()), str(self.ui.combo_ctrgrp.currentText())]
        self.analysis_paramsgui.cvthresh = float(self.ui.lineEdit_cvthresh.text())
        if self.ui.radioButton_meancv.isChecked():
            self.analysis_paramsgui.cvparam = 'average CV'
        else:
            self.analysis_paramsgui.cvparam = 'median CV'
            
        
        self.analysis_paramsgui.PCA = self.ui.checkBox_pca.isChecked()
        self.analysis_paramsgui.Dendrogram = self.ui.checkBox_dend.isChecked()
        self.analysis_paramsgui.bootstrap = self.dialog.ui.checkBox_bootstrap.isChecked()
        self.analysis_paramsgui.MZRTplt = self.ui.checkBox_mzrt.isChecked()
        self.analysis_paramsgui.KMD = self.ui.checkBox_kmd.isChecked()
        self.analysis_paramsgui.mdguide = self.dialog.ui.checkBox_mdguide.isChecked()
        self.analysis_paramsgui.FC = self.ui.checkBox_fc.isChecked()
        self.analysis_paramsgui.FC3Dplt = self.ui.checkBox_3dfc.isChecked()
        self.analysis_paramsgui.Ttest = self.ui.checkBox_ttest.isChecked()
        self.analysis_paramsgui.Volcanoplt = self.ui.checkBox_volcano.isChecked()
        self.analysis_paramsgui.pqthresh = float(self.dialog.ui.lineEdit_pqthresh.text())
        self.analysis_paramsgui.fcthresh = float(self.dialog.ui.lineEdit_fcthresh.text())
        self.analysis_paramsgui.colorscheme = self.dialog.ui.combo_colorscheme.currentText()
        self.analysis_paramsgui.FDR = self.ui.checkBox_FDR.isChecked()
        self.analysis_paramsgui.relfil = self.ui.checkBox_mp.isChecked()
        self.analysis_paramsgui.CVfil = self.ui.checkBox_cv.isChecked()
        self.analysis_paramsgui.decon = self.ui.checkBox_decon.isChecked()
        self.analysis_paramsgui.merge = self.ui.checkBox_merge.isChecked()
        self.analysis_paramsgui.RTwin = float(self.ui.lineEdit_rtwin.text())
        self.analysis_paramsgui.ringingwin = float(self.ui.lineEdit_ringwin.text())
        self.analysis_paramsgui.isopeakwin = float(self.ui.lineEdit_isowin.text())
        self.analysis_paramsgui.dimerpeakwin = float(self.ui.lineEdit_isowin.text())
        self.analysis_paramsgui.maxisowin = float(self.ui.combo_maxisoshift.currentText())
        self.analysis_paramsgui.grpave = True
        self.analysis_paramsgui.prperr = True
        self.analysis_paramsgui.blnkfltr = self.ui.checkBox_blankfilter.isChecked()
        
        if self.ui.radioButton_blankfilter_abs.isChecked():
            self.analysis_paramsgui.blankfilparam = 'absolute'
            self.analysis_paramsgui.blankfilthresh = float(self.ui.lineEdit_blankfilter_absthresh.text())
        else:
            self.analysis_paramsgui.blankfilparam = 'relative'
            self.analysis_paramsgui.blankfilthresh = float(self.ui.lineEdit_blankfilter_relthresh.text())
        if self.ui.checkBox_blankfilter.isChecked() and self.analysis_paramsgui.blnkgrp == '':
            self.analysis_paramsgui.blnkgrp = 'Blanks'
        self.analysis_paramsgui.ppmthresh = float(self.ui.lineEdit_ppmthresh.text())
    
    
    def regenerateplts(self):
        pltfile = self.analysis_paramsgui.outputdir / (self.analysis_paramsgui.filename.stem + '_filtered.csv')
        dfs = self.filtereddfs
        grpsts = self.groupsets
    
        if self.analysis_paramsgui.CVfil:
            self.prevcv.reset(self, '', '')
            stop_functime('cvplt complete')
    
        self.ftplt.reset(self.analysis_paramsgui.outputdir / 'iondict.csv', '', '')
        stop_functime('ftplt complete')
    
        self.dend.reset(pltfile, '', '')
        stop_functime('dendrogram complete')
    
        if self.analysis_paramsgui.PCA:
            self.pca.reset(pltfile, '', '')
            stop_functime('nmds complete')
    
        if self.analysis_paramsgui.FC3Dplt:
            self.fc3d.reset(self.analysis_paramsgui.outputdir / 'iondict.csv', dfs, grpsts)
            stop_functime('fc3d complete')
    
        if self.analysis_paramsgui.KMD:
            self.kmd.reset(self.analysis_paramsgui.outputdir / 'iondict.csv', dfs, grpsts)
            stop_functime('kmd complete')
    
        if self.analysis_paramsgui.MZRTplt:
            self.mzrt.reset(self.analysis_paramsgui.outputdir / 'iondict.csv', dfs, grpsts)
            stop_functime('mzrt complete')
    
        if self.analysis_paramsgui.Volcanoplt:
            self.volcano.reset(self.analysis_paramsgui.outputdir / 'iondict.csv', dfs, grpsts)
            stop_functime('volcano complete')
    
        self.heatmap.reset(self,  'heatmap', self.ui.frame_heatmap, pltfile)
        stop_functime('heatmap complete')
    
        self.samplecorr.reset(self.analysis_paramsgui.outputdir / 'iondict.csv', dfs, grpsts)
        stop_functime('samplecorr complete')
    
        self.ui.label_status.setText('Update Complete')

        

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if sys.platform != 'win32':
        app.setStyle('Fusion')
    app.setStyleSheet("QFrame { border: 0px; }") #QToolTip { color: #999999; background-color: rgb(0, 255, 0); border: 1px solid grey; }")
    window = MainWindow()
    sys.exit(app.exec_())
