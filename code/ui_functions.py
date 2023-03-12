"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

## ==> GUI FILE
from main import MainWindow, query, start_functime, stop_functime, reset_runtime, ftrdialog, dialog
#import masstdriver #from old version of masst search push
import webbrowser #may not be needed now
from mzmineimport import format_check

# CHECK/IMPORT DEPENDENCIES
from importdependencies import checkdep
checkdep()

import sys
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import time

import platform
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QFileDialog, QListWidgetItem, QColorDialog
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import QBrush, QColor, QIcon, QPalette, QPainter, QPixmap
from pathlib import Path


# IMPORT FUNCTIONS AND RESOURCES
import files

from MSFaST import analysis_parameters

import os




## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            #self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(34, 34, 34, 255), stop:1 rgba(52, 52, 52, 255));")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            #self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10) #not sure about this one throws error when run, may cut
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(34, 34, 34, 255), stop:1 rgba(52, 52, 52, 255));")
            self.ui.btn_maximize.setToolTip("Maximize")
            

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        #self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # Top bar functions
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())

        #mainbar functions
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.btn_import.clicked.connect(lambda: UIFunctions.goto_import(self))
        self.ui.btn_filter.clicked.connect(lambda: UIFunctions.goto_filter(self))
        self.ui.btn_parameters.clicked.connect(lambda: UIFunctions.goto_params(self))
        self.ui.btn_plots.clicked.connect(lambda: UIFunctions.goto_plot(self))
        self.ui.btn_info.clicked.connect(lambda: UIFunctions.goto_info(self))
        self.ui.btn_search.clicked.connect(lambda: UIFunctions.goto_search(self))

        #plotbar functions
        self.ui.stackedWidget_plot.setCurrentIndex(0)
        self.ui.btn_review.clicked.connect(lambda: UIFunctions.goto_review(self))
        self.ui.btn_upset.clicked.connect(lambda: UIFunctions.goto_upset(self))
        self.ui.btn_dend.clicked.connect(lambda: UIFunctions.goto_dend(self))
        self.ui.btn_pca.clicked.connect(lambda: UIFunctions.goto_pca(self))
        self.ui.btn_mzrt.clicked.connect(lambda: UIFunctions.goto_mzrt(self))
        self.ui.btn_kmd.clicked.connect(lambda: UIFunctions.goto_kmd(self))
        self.ui.btn_3dfc.clicked.connect(lambda: UIFunctions.goto_3dfc(self))
        self.ui.btn_volcano.clicked.connect(lambda: UIFunctions.goto_volcano(self))
        self.ui.btn_heatmap.clicked.connect(lambda: UIFunctions.goto_heatmap(self))
        
        self.ui.stackedWidget_review.setCurrentIndex(3)
        self.ui.btn_ftrplt.clicked.connect(lambda: self.ui.stackedWidget_review.setCurrentIndex(0))
        self.ui.btn_treemap.clicked.connect(lambda: self.ui.stackedWidget_review.setCurrentIndex(1))
        self.ui.btn_cvplt.clicked.connect(lambda: self.ui.stackedWidget_review.setCurrentIndex(2))
        self.ui.btn_datasummary.clicked.connect(lambda: self.ui.stackedWidget_review.setCurrentIndex(3))
        
        self.ui.btn_upsetplt.clicked.connect(lambda: self.ui.stackedWidget_grpanalysis.setCurrentIndex(0))
        self.ui.btn_samplecorr.clicked.connect(lambda: self.ui.stackedWidget_grpanalysis.setCurrentIndex(1))

        #feature info bar functions
        self.ftrdialog.ui.btn_close.clicked.connect(lambda: self.ftrdialog.hide())  
        self.ftrdialog.ui.btn_hits.clicked.connect(lambda: UIFunctions.goto_hits(self)) 
        self.ftrdialog.ui.btn_abund.clicked.connect(lambda: UIFunctions.goto_abund(self))
        self.ftrdialog.ui.btn_spectrum.clicked.connect(lambda: UIFunctions.goto_spectrum(self)) 
        self.ftrdialog.ui.btn_masst.clicked.connect(lambda: UIFunctions.masst(self)) 
        self.ui.btn_details.clicked.connect(lambda: UIFunctions.show_ftrdialog(self)) 
        self.ui.btn_details_2.clicked.connect(lambda: UIFunctions.show_ftrdialog(self)) 
        
        #input functions
        self.ui.btn_load_session.clicked.connect(lambda: UIFunctions.loadsession(self))
        self.ui.btn_import_pktbl.clicked.connect(lambda: UIFunctions.getfilename(self))
        self.ui.btn_import_spllist.clicked.connect(lambda: UIFunctions.getsamplelistfilename(self))
        self.ui.btn_import_splmdt.clicked.connect(lambda: UIFunctions.getextractmetadatafilename(self))
        self.ui.btn_import_outdir.clicked.connect(lambda: UIFunctions.getoutputdir(self))
        self.ui.btn_import_msp.clicked.connect(lambda: UIFunctions.getfragfilename(self))
        
        #colour picker functions
        self.ui.btn_col1.clicked.connect(lambda: UIFunctions.colour_picker1(self))

        self.ui.btn_addgroup.clicked.connect(lambda: UIFunctions.addgroup(self))
        self.ui.btn_removegroup.clicked.connect(lambda: UIFunctions.removegroup(self))
        self.ui.listWidget_pltgrps.currentItemChanged.connect(lambda: UIFunctions.writegroups(self))

        #dialog functions and parameters
        self.dialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.dialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.dialog.ui.btn_close.clicked.connect(lambda: self.dialog.hide())
        self.dialog.ui.btn_apply.clicked.connect(self.regenerateplts)
        
        self.ftrdialog.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ftrdialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.ftrdialog.ui.treeWidget.hideColumn(5)
        self.ui.treeWidget.hideColumn(5) #hide sets column for now
        self.ftrdialog.hide()
        self.ftrdialog.ui.btn_related.hide()
        
        
        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip_corner)
        self.ui.frame_grip_corner.setStyleSheet("background: transparent; background-image: url(:/resources/icons/24x24/resize.png); background-position: center; background-repeat: no-repeat;" )
        self.sizegrip.setToolTip("Resize Window")


    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE


    #ui buttons
    def goto_import(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        UIFunctions.reset_mainbar(self)
        self.ui.btn_import.setStyleSheet(self.ui.mainbar_activebtn)
        
    def goto_filter(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        UIFunctions.reset_mainbar(self)
        self.ui.btn_filter.setStyleSheet(self.ui.mainbar_activebtn)       
        
    def goto_params(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        UIFunctions.reset_mainbar(self)
        self.ui.btn_parameters.setStyleSheet(self.ui.mainbar_activebtn)

    def goto_plot(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        UIFunctions.reset_mainbar(self)
        self.ui.btn_plots.setStyleSheet(self.ui.mainbar_activebtn)

    def goto_info(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        UIFunctions.reset_mainbar(self)
        self.ui.btn_info.setStyleSheet(self.ui.mainbar_activebtn)
        
    def goto_search(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        UIFunctions.reset_mainbar(self)
        self.ui.btn_search.setStyleSheet(self.ui.mainbar_activebtn)
        #self.ftrdialog.show()
        if self.dbsearchdone == False and self.analysisrun:
            start_functime()
            self.fulldbsearch()
            self.fillfttree()
            self.dbsearchdone = True
            stop_functime('dbsearch complete')
            reset_runtime()
            
    #plotbar functions
    def goto_review(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(0)
        self.ui.stackedWidget_plot.setCurrentIndex(1)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_review.setStyleSheet(self.ui.plotbar_activebtn)
        
        self.dialog.ui.checkBox_applyfilter.hide()

    def goto_upset(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(1)
        self.ui.stackedWidget_plot.setCurrentIndex(9)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_upset.setStyleSheet(self.ui.plotbar_activebtn)
        
        self.dialog.ui.checkBox_applyfilter.hide()
        self.dialog.ui.frame_colorscheme.show()
        
    def goto_dend(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(1)
        self.ui.stackedWidget_plot.setCurrentIndex(2)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_dend.setStyleSheet(self.ui.plotbar_activebtn)
        
    def goto_pca(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(1)
        self.ui.stackedWidget_plot.setCurrentIndex(3)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_pca.setStyleSheet(self.ui.plotbar_activebtn)
        
        self.dialog.ui.frame_2.show()

    def goto_mzrt(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(0)
        self.ui.stackedWidget_plot.setCurrentIndex(4)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_mzrt.setStyleSheet(self.ui.plotbar_activebtn)
        
    def goto_kmd(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(0)
        self.ui.stackedWidget_plot.setCurrentIndex(5)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_kmd.setStyleSheet(self.ui.plotbar_activebtn)
        
        self.dialog.ui.frame_mdguide.show()
        
    def goto_3dfc(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(0)
        self.ui.stackedWidget_plot.setCurrentIndex(6)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_3dfc.setStyleSheet(self.ui.plotbar_activebtn)
        
    def goto_volcano(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(0)
        self.ui.stackedWidget_plot.setCurrentIndex(7)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_volcano.setStyleSheet(self.ui.plotbar_activebtn)
        
        self.dialog.ui.frame_volcanoparams.show()

    def goto_heatmap(self):
        self.ui.stackedWidget_infobar.setCurrentIndex(0)
        self.ui.stackedWidget_plot.setCurrentIndex(8)
        UIFunctions.reset_plotbar(self)
        self.ui.btn_heatmap.setStyleSheet(self.ui.plotbar_activebtn)

        self.dialog.ui.frame_colorscheme.show()
        
    #ftinfobar functions
    def goto_abund(self):
        self.ftrdialog.ui.btn_masst.hide()
        self.ftrdialog.ui.stackedWidget.setCurrentIndex(2)
        self.highlight_feature(self.pickedfeature)
        self.ftrdialog.ui.btn_abund.setStyleSheet(self.ui.ftbar_activebtn)
        
    def goto_hits(self):
        self.ftrdialog.ui.btn_masst.hide()
        self.ftrdialog.ui.stackedWidget.setCurrentIndex(0)
        self.highlight_feature(self.pickedfeature)
        UIFunctions.reset_ftrdialogbar(self)
        self.ftrdialog.ui.btn_hits.setStyleSheet(self.ui.ftbar_activebtn)
        
    def goto_spectrum(self):
        self.ftrdialog.ui.btn_masst.show()
        self.ftrdialog.ui.stackedWidget.setCurrentIndex(1)
        UIFunctions.reset_ftrdialogbar(self)
        self.ftrdialog.ui.btn_spectrum.setStyleSheet(self.ui.ftbar_activebtn)

    def masst(self): 
        """
        Launches the web browser and searches for mass spectra of selected feature in Mass Spectrometry Interactive Virtual Environment (MassIVE).
        
        Args:
            None
        
        Returns:
            None
        """
        if self.fragdb != 'None' and self.fragdb.ions[self.pickedfeature].pattern.shape[0] > 0:
            description = str("MPACT_SUBMISSION:" + self.analysis_paramsgui.filename.stem + "_" + self.pickedfeature)
            precursor = str(self.fragdb.ions[self.pickedfeature].fragparams['PrecursorMZ']).strip()
            fragments = ''
            for row in self.fragdb.ions[self.pickedfeature].pattern:
                fragments = fragments + str(row[0]) + r'\t' + str(row[1]) + r'\n'
            url = r'''https://gnps.ucsd.edu/ProteoSAFe/index.jsp#{%22workflow%22:%22SEARCH_SINGLE_SPECTRUM%22,%22precursor_mz%22:"'''
            url = url + precursor + r'''%22,%22spectrum_string%22:"'''
            url = url + fragments + r'''%22,%22desc%22:"'''
            url = url + description + r'''%22}'''
            #print(url)
            webbrowser.open(url)

            #used for external version with nonlogin masst            
            #masstdriver.push(description, precursor, fragments)

    #colour buttons
    def colour_picker1(self):
        """
        Allows user to pick a color from color dialog and sets the selected color to the selected query set's color attribute.

        """
        color = QColorDialog.getColor()
        self.querys[self.selset].colour = color.name() 
        self.ui.btn_col1.setStyleSheet("QPushButton {border: 2px solid lightgrey; background-color: " + str(self.querys[self.selset].colour) +";}")
    
    def updatesets(self):
        """
        Updates the list of query sets in the GUI and sets the selected query set.

        """
        selitem = self.ui.listWidget_pltgrps.currentRow() - 1
        selitem = max(selitem, 0)
        
        self.ui.listWidget_pltgrps.clear()
        for query in self.querys:
            item = QListWidgetItem(query.name)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            self.ui.listWidget_pltgrps.addItem(item)
    
        self.ui.listWidget_pltgrps.setCurrentRow(selitem)
        UIFunctions.updategroups(self)
        
    
    def updategroups(self):
        """
        Updates the lists of groups for the selected query set in the GUI.
        """
        selgroup = self.ui.listWidget_pltgrps.currentRow()
        self.selset = selgroup
    
        self.ui.listWidget_allgrps.clear()
        self.ui.listWidget_orgrps.clear()
        self.ui.listWidget_andgrps.clear()
    
        for group in self.querys[selgroup].excl:
            self.ui.listWidget_allgrps.addItem(QListWidgetItem(group))
        for group in self.querys[selgroup].src:
            self.ui.listWidget_orgrps.addItem(QListWidgetItem(group))
        for group in self.querys[selgroup].incl:
            self.ui.listWidget_andgrps.addItem(QListWidgetItem(group))
    
        self.ui.btn_col1.setStyleSheet(
            "QPushButton {border: 2px solid lightgrey; background-color: " + 
            str(self.querys[self.selset].colour) +";}"
        )
    
    def writegroups(self):
        """
        Writes the changes made to the query set's name, included groups, excluded groups, and source groups in the GUI to the query object.
        """
        if 0 <= self.selset < self.ui.listWidget_pltgrps.count():
            try:
                self.querys[self.selset].name = self.ui.listWidget_pltgrps.item(self.selset).text()
            except Exception:
                pass
    
            self.querys[self.selset].excl = [self.ui.listWidget_allgrps.item(x).text() for x in range(self.ui.listWidget_allgrps.count())]
            self.querys[self.selset].src = [self.ui.listWidget_orgrps.item(x).text() for x in range(self.ui.listWidget_orgrps.count())]
            self.querys[self.selset].incl = [self.ui.listWidget_andgrps.item(x).text() for x in range(self.ui.listWidget_andgrps.count())]
    
        UIFunctions.updategroups(self)
        
        
    def addgroup(self, name = 'New Feature Set'):
        """
        Adds a new query set to the list of query sets in the GUI and to the querys list.
        """
        item = QListWidgetItem(name)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        
        self.ui.listWidget_pltgrps.addItem(item)
        item.setSelected(True)
        
        currquery = query()
        currquery.name = item.text()
        currquery.src = []
        currquery.incl = []
        currquery.excl = []
        currquery.color = '#000000'
        
        for group in self.groups:
            currquery.excl.append(group)
            
        self.querys.append(currquery)
        self.ui.listWidget_pltgrps.setCurrentItem(item)

            
    def removegroup(self):
        """
        Removes the selected query set from the list of query sets in the GUI and from the querys list.
        """
        selitem = self.ui.listWidget_pltgrps.currentRow()
        self.querys.remove(self.querys[selitem])
        UIFunctions.updatesets(self)
        
        
        
    #import buttons
    def loadsession(self):
            """
            Displays a file dialog to get the saved session file, calls the `read_save` method in `main.py` to read the saved 
            data and updates the UI elements with the saved parameters.
            """
            try:
                self.savefile, _  = QFileDialog.getOpenFileName(self, 'Open file', self.recentdir , 
                                                                               "*.mpct")
                self.savefile = Path(self.savefile)
                self.recentdir = str(self.savefile.parent)
                self.read_save(self.savefile)
                
                self.ui.lbl_pktbl.setText(self.filename.name)
                self.ui.lbl_spllist.setText(self.samplelistfilename.name)
                self.ui.lbl_splmdt.setText(self.extractmetadatafilename.name)
                self.ui.lbl_msp.setText(self.fragfilename.name)
                if len(str(self.outputdir)) <40:
                    self.ui.lbl_outdir.setText(self.outputdir)
                else:
                    self.ui.lbl_outdir.setText('...' + str(self.outputdir)[-40:])
                
                self.ui.checkBox_cv.setChecked('cv' in self.analysis_paramsgui.graphfilters) # may be good to add seperate parameters for each filter instead of using str?
                self.ui.radioButton_meancv.setChecked('average' in self.analysis_paramsgui.cvparam)
                self.ui.radioButton_medcv.setChecked('median' in self.analysis_paramsgui.cvparam)
                self.ui.lineEdit_cvthresh.setText(str(self.analysis_paramsgui.cvthresh))
                self.ui.checkBox_mp.setChecked('rel' in self.analysis_paramsgui.graphfilters)
                self.ui.lineEdit_rtwin.setText(str(self.analysis_paramsgui.RTwin))
                self.ui.lineEdit_isowin.setText(str(self.analysis_paramsgui.isopeakwin))
                self.ui.combo_maxisoshift.setCurrentIndex(self.analysis_paramsgui.maxisowin)
                self.ui.checkBox_decon.setChecked('insource' in self.analysis_paramsgui.graphfilters)
                self.ui.lineEdit_insourcethresh.setText(str(self.analysis_paramsgui.deconthresh))
                self.ui.checkBox_blankfilter.setChecked(self.analysis_paramsgui.blnkfltr)
                self.ui.combo_blankfil_name.setCurrentText(str(self.analysis_paramsgui.blnkgrp))
                self.ui.radioButton_meancv.setChecked('average' in self.analysis_paramsgui.cvparam)
                if 'absolute' in self.analysis_paramsgui.blankfilparam:
                    self.ui.lineEdit_blankfilter_absthresh.setText(str(self.analysis_paramsgui.blankfilthresh))
                    self.ui.radioButton_blankfilter_abs.setChecked(True)
                else:
                    self.ui.lineEdit_blankfilter_relthresh.setText(str(self.analysis_paramsgui.blankfilthresh))
                    self.ui.radioButton_blankfilter_rel.setChecked(True)
    
                self.ui.checkBox_pca.setChecked(self.analysis_paramsgui.PCA)
                self.ui.checkBox_dend.setChecked(self.analysis_paramsgui.Dendrogram)
                self.dialog.ui.checkBox_bootstrap.setChecked(self.analysis_paramsgui.bootstrap)
                self.ui.checkBox_mzrt.setChecked(self.analysis_paramsgui.MZRTplt)
                self.ui.checkBox_kmd.setChecked(self.analysis_paramsgui.KMD)
                self.ui.checkBox_fc.setChecked(self.analysis_paramsgui.FC)
                self.ui.checkBox_3dfc.setChecked(self.analysis_paramsgui.FC3Dplt)
                self.ui.checkBox_ttest.setChecked(self.analysis_paramsgui.Ttest)
                self.ui.checkBox_volcano.setChecked(self.analysis_paramsgui.Volcanoplt)
                self.ui.checkBox_FDR.setChecked(self.analysis_paramsgui.FDR)
                self.ui.combo_expgrp.setCurrentText(str(self.analysis_paramsgui.statstgrps[0]))
                self.ui.combo_ctrgrp.setCurrentText(self.analysis_paramsgui.statstgrps[1])
                
                self.dialog.ui.combo_colorscheme.setCurrentText(self.analysis_paramsgui.colorscheme)
                self.dialog.ui.lineEdit_pqthresh.setText(str(self.analysis_paramsgui.pqthresh))
                self.dialog.ui.lineEdit_fcthresh.setText(str(self.analysis_paramsgui.fcthresh))
                self.dialog.ui.checkBox_mdguide.setChecked(self.analysis_paramsgui.mdguide)
            except Exception:
               #self.error('Files in use, Close before analysis')
               pass
               return()
                
    def getfilename(self):
            self.filename, _  = QFileDialog.getOpenFileName(self, 'Open file', self.recentdir ,
                                                                           "*.csv *.txt")
            self.filename = Path(self.filename)
            self.recentdir = str(self.filename.parent)
            self.ui.lbl_pktbl.setText(self.filename.name)
            format_check(self)
            if self.filename.suffix == '.csv' and self.extractmetadatafilename.suffix == '.csv' and self.samplelistfilename.suffix == '.csv':
                self.getgroups() 

    def getsamplelistfilename(self):
            self.samplelistfilename, _ = QFileDialog.getOpenFileName(self, 'Open file', self.recentdir ,
                                                                           "*.csv")
            self.samplelistfilename = Path(self.samplelistfilename)
            self.recentdir = str(self.samplelistfilename)
            self.ui.lbl_spllist.setText(self.samplelistfilename.name) 
            if self.filename.suffix == '.csv' and self.extractmetadatafilename.suffix == '.csv' and self.samplelistfilename.suffix == '.csv':
                self.getgroups() 

    def getextractmetadatafilename(self):
            self.extractmetadatafilename, _ = QFileDialog.getOpenFileName(self, 'Open file', self.recentdir ,
                                                                           "*.csv")
            self.extractmetadatafilename = Path(self.extractmetadatafilename)
            self.recentdir = str(self.extractmetadatafilename)
            self.ui.lbl_splmdt.setText(self.extractmetadatafilename.name)
            if self.filename.suffix == '.csv' and self.extractmetadatafilename.suffix == '.csv' and self.samplelistfilename.suffix == '.csv':
                self.getgroups() 
                
    def getoutputdir(self):
            self.outputdir = Path(str(QFileDialog.getExistingDirectory(self, 'Select Directory', self.recentdir)))
            self.recentdir = str(self.outputdir)
            if len(str(self.outputdir)) <40:
                try:
                    self.ui.lbl_outdir.setText(self.outputdir)
                except Exception:
                    self.error('No directory selected')
                    pass
                    return()
            else:
                self.ui.lbl_outdir.setText('...' + str(self.outputdir)[-40:])

    def getfragfilename(self):
            self.fragfilename, _ = QFileDialog.getOpenFileName(self, 'Open file', self.recentdir,
                                                                           "*.msp")
            self.recentdir = str(self.outputdir)
            self.fragfilename = Path(self.fragfilename)
            self.ui.lbl_msp.setText(self.fragfilename.name)


    #reset uibar buttons
    def reset_mainbar(self):
        self.ui.mainbar_activebtn = "QPushButton {	border: none; background-color: transparent;}QPushButton:hover {background-color: transparent}QPushButton:pressed {	background-color: rgb(75, 75, 75);}"
        self.ui.mainbar_inactivebtn ="QPushButton {	border: none; background-color: rgb(35, 35, 35);}QPushButton:hover {background-color: transparent}QPushButton:pressed {	background-color: rgb(75, 75, 75);}"
        self.ui.btn_import.setStyleSheet(self.ui.mainbar_inactivebtn)
        self.ui.btn_filter.setStyleSheet(self.ui.mainbar_inactivebtn)
        self.ui.btn_parameters.setStyleSheet(self.ui.mainbar_inactivebtn)
        self.ui.btn_plots.setStyleSheet(self.ui.mainbar_inactivebtn)
        self.ui.btn_info.setStyleSheet(self.ui.mainbar_inactivebtn)
        self.ui.btn_search.setStyleSheet(self.ui.mainbar_inactivebtn)
        self.ui.label_status.setText('') #to reset analysis status after tabs are switched. eventually use a second thread to dynamically update status
        self.ui.label_status.setStyleSheet('color: rgb(150,150,150);')
        
    def reset_plotbar(self):
        self.ui.plotbar_activebtn = "QPushButton {	border: none;background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)} QPushButton:hover {background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)} QPushButton:pressed {	 background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)}"
        self.ui.plotbar_inactivebtn ="QPushButton {	border: none;background-color: rgba(0,0,0, 0)} QPushButton:hover {background-color: rgba(225,225,225, 50)} QPushButton:pressed {	 background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)}"
        self.ui.btn_review.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_dend.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_upset.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_pca.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_mzrt.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_kmd.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_3dfc.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_volcano.setStyleSheet(self.ui.plotbar_inactivebtn)
        self.ui.btn_heatmap.setStyleSheet(self.ui.plotbar_inactivebtn)
        
        self.dialog.ui.frame_2.hide()
        self.dialog.ui.frame.hide() #hide apply button, button doesnt work right now, use run button
        self.dialog.ui.frame_mdguide.hide()
        self.dialog.ui.frame_volcanoparams.hide()
        self.dialog.ui.frame_colorscheme.hide()
        self.dialog.ui.checkBox_applyfilter.show()
        self.ui.label_status.setText('')

    def reset_ftrdialogbar(self):
        self.ui.ftbar_activebtn = "QPushButton {border: none;background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)} QPushButton:hover {background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)} QPushButton:pressed {	 background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)}"
        self.ui.ftbar_inactivebtn ="QPushButton {border: none;background-color: rgba(0,0,0,0)} QPushButton:hover {background-color: rgba(225,225,225, 50)} QPushButton:pressed {	 background-color: rgba(225,225,225, 255);	color: rgba(75,75,75,255)}"
        self.ftrdialog.ui.btn_hits.setStyleSheet(self.ui.ftbar_inactivebtn)
        self.ftrdialog.ui.btn_spectrum.setStyleSheet(self.ui.ftbar_inactivebtn)
        self.ftrdialog.ui.btn_abund.setStyleSheet(self.ui.ftbar_inactivebtn)
    
    def show_ftrdialog(self):
        self.ftrdialog.show()
        if self.pickedfeature != '':
            self.highlight_feature(self.pickedfeature)

