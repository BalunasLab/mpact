"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import numpy as np
import pandas as pd

import matplotlib
#matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt
plt.ioff()
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT)
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import seaborn as sns
import squarify # pip install squarify
import upsetplot
#plt.rc('xtick',labelsize=16)
#plt.rc('ytick',labelsize=16)

import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QIcon, QPalette, QPainter, QPixmap)
from PyQt5.QtWidgets import *
from pathlib import Path

import scipy.cluster.hierarchy as shc
from sklearn.preprocessing import normalize
from sklearn import manifold
from sklearn.metrics import pairwise_distances
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib.patches import Ellipse
from filter import listfilter
import time

from pvclust import PvClust

class NavigationToolbar(NavigationToolbar2QT): #subclassed plot toolbar with extra button
        def __init__(self, canvas, parent):
            NavigationToolbar2QT.__init__(self,canvas,parent)
            self.clearButtons=[]
            next=None
            for c in self.findChildren(QToolButton):
                if next is None:
                    next=c
                if str(c.text()) in ('Pan','Zoom','Subplots'):
                    self.clearButtons.append(c)
                    next=None 
            # create custom button
            pm=QPixmap(32,32)
            pm.fill(QtWidgets.QApplication.palette().color(QPalette.Normal,QPalette.Button))
            painter=QPainter(pm)
            painter.fillRect(6,6,20,20,Qt.black)
            painter.end()
            icon=QIcon(pm)
            picker=QAction("Pick",self)
            picker.setIcon(icon)
            picker.setToolTip("Configure")
            self.picker = picker
            button=QToolButton(self)
            button.setDefaultAction(self.picker) 
            button.clicked.connect(lambda: parent.dialog.show())
            self.addWidget(button)
        
#General plot method#
class ui_plot: #subclassed for individual plots
    def __init__(self, parent, currplt, frame): #initialization of general params for all plots
        parent.fig[currplt] = Figure()
        parent.pltlayout[currplt] = QtWidgets.QVBoxLayout()
        parent.canvas[currplt] = FigureCanvas(parent.fig[currplt])
        parent.pltlayout[currplt].addWidget(parent.canvas[currplt])
        parent.toolbar[currplt] = NavigationToolbar(parent.canvas[currplt], parent)
        parent.toolbar[currplt].setStyleSheet("background-color:rgba(225,225,225,0);")
        parent.pltlayout[currplt].addWidget(parent.toolbar[currplt])
        frame.setLayout(parent.pltlayout[currplt])
        parent.ax[currplt] = parent.canvas[currplt].figure.subplots()  
        parent.ax[currplt].set_axisbelow(True)

        self.fcsfont = {'fontname':'Bahnschrift',
                'weight' : 'bold',
                'size'   : 20}
        self.fhfont = {'fontname':'Bahnschrift',
                'weight' : 'bold',
                'size'   : 25}
        self.plotbackground = (.89, .89, .89, 0)
        parent.canvas[currplt].figure.set_facecolor(self.plotbackground)
        parent.ax[currplt].set_facecolor(self.plotbackground)

    def onpick(self, event, parent, iondict, plotcols): #general feature selection, changed for heatmap
        ind = event.ind
        coord = event.artist.get_offsets()[ind,:]
        pickedfeature = iondict.loc[iondict[plotcols[0]] == coord[0,0], :].loc[iondict[plotcols[1]] == coord[0,1], :]
        parent.ui.lbl_featurename.setText('Compound: ' + str(pickedfeature.iloc[0,0]))
        parent.ui.lbl_featurert.setText('Retention time: ' + str(round(pickedfeature.iloc[0,2], 4)))
        parent.ui.lbl_featuremz.setText('m/z: ' + str(round(pickedfeature.iloc[0,1], 4)))
        pickedfeature = str(pickedfeature.iloc[0,0])
        parent.highlight_feature(pickedfeature)
        
    def reset(self, file, filtereddfs, groupsets): # resets plot on rerun of analysis
                # need to do something with kwargs to allow different inputs for plot() based on what is needed
        self.parent.ax[self.currplt].clear()
        self.parent.canvas[self.currplt].draw()
        self.plot(self.parent, file, filtereddfs, groupsets)
    
#subclassed plot methods
class plot_abund(): #abundance plot made of barchart and strip/point plots
    def __init__(self, parent, currplt): #this is needed since two plots are included
        self.parent = parent
        self.currplt = currplt
        parent.fig[currplt] = Figure()
        parent.pltlayout[currplt] = QtWidgets.QVBoxLayout()
        parent.canvas[currplt] = FigureCanvas(parent.fig[currplt])
        parent.pltlayout[currplt].addWidget(parent.canvas[currplt])
        parent.toolbar[currplt] = NavigationToolbar(parent.canvas[currplt], parent)
        parent.toolbar[currplt].setStyleSheet("background-color:rgba(225,225,225,0);")
        parent.pltlayout[currplt].addWidget(parent.toolbar[currplt])
        parent.ftrdialog.ui.frame_abundance.setLayout(parent.pltlayout[currplt])
        parent.ax[currplt] = parent.canvas[currplt].figure.subplots(ncols=2)  
        
        self.plotbackground = (.89, .89, .89, 0)
        parent.canvas[currplt].figure.set_facecolor(self.plotbackground)
        self.fcsfont = {'fontname':'Bahnschrift',
                'weight' : 'bold',
                'size'   : 12}
        self.fhfont = {'fontname':'Bahnschrift',
                'weight' : 'bold',
                'size'   : 25}
        
    def plot(self, parent): #this could be made faster with a refactor
        #get header info
        currplt = self.currplt
        msdata = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = [0, 1, 2], index_col = [0]).iloc[:, 2:].loc[parent.pickedfeature]
        msdata = msdata.reset_index()
        msdata.columns = ['biolgroup','sample','injection','abundance']
        msdata = msdata.drop(columns=['injection'])
        
        #gets stats for the given ion
        summary = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_summarydata.csv'), sep = ',', header = [0, 1], index_col = [0]).iloc[:, 2:].loc[parent.pickedfeature]
        combasd = summary.loc[['combASD']].to_frame()
        combasd.index = combasd.index.droplevel(level = 0)
        neff = summary.loc[['neff']].to_frame()
        neff.index = neff.index.droplevel(level = 0)
        ionsummary = summary.loc[['average']]
        ionsummary.index = ionsummary.index.droplevel(level = 0)

        ionsummary = ionsummary.to_frame()
        ionsummary.columns = ['average']
        ionsummary['combASD'] = combasd
        ionsummary['neff'] = neff
        if parent.analysis_paramsgui.blnkfltr: #need to not explicitly call blanks, call the value in the params
            ionsummary = ionsummary.drop([parent.analysis_paramsgui.blnkgrp], axis=0)
        ionsummary = ionsummary.reset_index()

        #make plots for the features, strip and pointplot are computationally expensive
        sns.barplot(ax=parent.ax[currplt][0], x="index", y="average", yerr=ionsummary["combASD"],
                    errcolor=".2", edgecolor=".2", data=ionsummary, zorder=1)
        parent.ax[currplt][1].set_xticklabels(parent.ax[currplt][1].get_xticklabels(), 
                                  rotation=90, 
                                  horizontalalignment='center')
        
        sns.stripplot(ax=parent.ax[currplt][1], x="sample", y="abundance", hue="biolgroup",
                      data=msdata, size = 7, dodge=False, alpha=.5, zorder=2)
        
        sns.pointplot(ax=parent.ax[currplt][1], x="sample", y="abundance", color = "#999999", #hue="sample",
                      data=msdata, dodge=False, join=False, #palette="dark",
                      markers="d", scale=.75, zorder=1, capsize = .1,
                      errwidth=1, ci=95)

        ylims = (0, parent.ax[currplt][1].get_ylim()[1]*1.05)
        parent.ax[currplt][0].set_ylim(ylims)
        parent.ax[currplt][1].set_ylim(ylims)
        parent.ax[currplt][1].legend_.remove()
        plt.tight_layout()
        plt.show()
        
    def reset(self):
        self.parent.ax[self.currplt][0].clear()
        self.parent.ax[self.currplt][1].clear()
        self.plot(self.parent)
        self.parent.canvas[self.currplt].draw()

class show_spectrum(ui_plot): #MS2 spectrum viewer
            #should add annotation to bars
    def __init__(self, parent, currplt):
        frame = parent.ftrdialog.ui.frame_spec
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        
    def plot(self, parent, frags): 
        parent.ax[self.currplt].vlines(frags[:,0], 0, frags[:,1], colors='k', linestyles='solid')
        parent.ax[self.currplt].set_xlabel('m/z',  **self.fcsfont)
        parent.ax[self.currplt].set_ylabel('Abundance',  **self.fcsfont)
        parent.ax[self.currplt].set_xlim(left=0)
        parent.ax[self.currplt].set_ylim(bottom=0)
        parent.canvas[self.currplt].draw()
        
    def reset(self, parent, frags): # need to do something with kwargs to allow different inputs for plot() based on what is needed MAYBE JUST RESET THE DATA SET OR AXIS DIRECTLY
        self.parent.ax[self.currplt].clear()
        self.parent.canvas[self.currplt].draw()
        self.plot(parent, frags)
        
class show_featureplt(ui_plot): #filtered feature plot
    def __init__(self, parent, currplt, frame, iondictloc, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, iondictloc, filtereddfs, groupsets)
        
    def plot(self, parent, iondictloc, filtereddfs, groupsets): # may be possible to improve feature selection from DFs
        iondict = pd.read_csv(iondictloc, sep = ',', header = [0], index_col = None)
        iondict['colour'] = '#000000' # colour map for features based on which filter they are caught by
        if parent.analysis_paramsgui.decon:
            iondict.loc[iondict['pass_insource'] == False, 'colour'] = '#00aa00'
        if parent.analysis_paramsgui.CVfil:
            iondict.loc[iondict[parent.analysis_paramsgui.cvparam] >= parent.analysis_paramsgui.cvthresh, 'colour'] = '#ff0000' #CHANGE BACK TO analysisparamasgui.cvthresh or whatever
        if parent.analysis_paramsgui.blnkfltr:
            iondict.loc[iondict['pass_blnkfil'] == False, 'colour'] = '#00aaaa'
        if parent.analysis_paramsgui.relfil:
            iondict.loc[iondict['pass_relfil'] == False, 'colour'] = '#0000ff'
    
        parent.a = parent.ax[self.currplt].scatter(iondict.loc[iondict['colour'] == '#0000ff', :]['Retention time (min)'], iondict.loc[iondict['colour'] == '#0000ff', :]['m/z'], color = '#0000ff', label="Mispicked", picker=True, alpha=.5)
        parent.ax[self.currplt].scatter(iondict.loc[iondict['colour'] == '#00aaaa', :]['Retention time (min)'], iondict.loc[iondict['colour'] == '#00aaaa', :]['m/z'], color = '#00aaaa', label="Blank features", picker=True, alpha=.5)
        parent.ax[self.currplt].scatter(iondict.loc[iondict['colour'] == '#ff0000', :]['Retention time (min)'], iondict.loc[iondict['colour'] == '#ff0000', :]['m/z'], color = '#ff0000', label="Nonreproducable", picker=True, alpha=.5)
        parent.ax[self.currplt].scatter(iondict.loc[iondict['colour'] == '#00aa00', :]['Retention time (min)'], iondict.loc[iondict['colour'] == '#00aa00', :]['m/z'], color = '#00aa00', label="In-source ions", picker=True, alpha=.5)
        parent.ax[self.currplt].scatter(iondict.loc[iondict['colour'] == '#000000', :]['Retention time (min)'], iondict.loc[iondict['colour'] == '#000000', :]['m/z'], color = '#000000', label="High Quality", picker=True, alpha=.5)
        parent.highlight[self.currplt], = parent.ax[self.currplt].plot([], [], 'o', markersize=12, color='yellow')
        parent.ax[self.currplt].set_xlabel('Retention time (min)',  **self.fcsfont)
        parent.ax[self.currplt].set_ylabel('m/z',  **self.fcsfont)
        parent.ax[self.currplt].set_xlim([0, 11])
        parent.ax[self.currplt].set_ylim([0, 2000])
        parent.ax[self.currplt].grid()
        parent.ax[self.currplt].legend()
        parent.canvas[self.currplt].figure.canvas.mpl_connect('pick_event', lambda event: self.onpick(event, parent, iondict, ('Retention time (min)', 'm/z')))
        parent.fig[self.currplt].subplots_adjust(left=.1,right=.95,
                            bottom=0.15,top=0.9,
                            hspace=0.2,wspace=0.2)
        parent.canvas[self.currplt].draw()

class plot_heatmap(): #heatmap
    def __init__(self, parent, currplt, frame, file):
        msdata = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = [2], index_col = [0]).iloc[:,2:]
        cm = sns.clustermap(msdata, standard_scale=0, metric="euclidean", method="ward", cmap = parent.analysis_paramsgui.colorscheme) #viridis
        parent.cmind = cm.dendrogram_row.reordered_ind #saves reordered index so that we can increment selection up and down.
        parent.fig[currplt] = cm.fig
        parent.pltlayout[currplt] = QtWidgets.QVBoxLayout()
        parent.canvas[currplt] = FigureCanvas(parent.fig[currplt])
        parent.pltlayout[currplt].addWidget(parent.canvas[currplt])
        parent.toolbar[currplt] = NavigationToolbar(parent.canvas[currplt], parent)
        parent.toolbar[currplt].setStyleSheet("background-color:rgba(225,225,225,255);")
        parent.pltlayout[currplt].addWidget(parent.toolbar[currplt])
        parent.ui.frame_heatmap.setLayout(parent.pltlayout[currplt])
        
        self.plotbackground = (.89, .89, .89, 0)
        parent.canvas[currplt].figure.set_facecolor(self.plotbackground)
        self.fcsfont = {'fontname':'Bahnschrift',
                'weight' : 'bold',
                'size'   : 12}
        self.fhfont = {'fontname':'Bahnschrift',
                'weight' : 'bold',
                'size'   : 25}
        parent.highlight[currplt], = parent.canvas[currplt].figure.axes[2].plot([], [], color='yellow', linestyle='-', linewidth=1)
    
        def onpick8(event): #rename
                # this gets the position of the selected item, finds the item in the reodered index,
                # and highlights the feature by name on other plots
            iondict = pd.read_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
            coord = [event.mouseevent.xdata,event.mouseevent.ydata]
            parent.heatind = int(np.floor(coord[1]))
            name = msdata.index.tolist()[parent.cmind[parent.heatind]]    
    
            parent.ui.lbl_featurename.setText('Compound: ' + name)
            parent.ui.lbl_featurert.setText('Retention time: ' + str(iondict.loc[name,'Retention time (min)']))
            parent.ui.lbl_featuremz.setText('m/z: ' + str(iondict.loc[name,'m/z']))
            parent.highlight_feature(name)
            
        def on_xlims_change(event_ax): #changes the limits of the x dendrogram when the heatmap is zoomed
            heatxlim = event_ax.get_xlim()
            yaxxlim = (10 * heatxlim[0], 10 * heatxlim[1])
            parent.canvas['heatmap'].figure.axes[1].set_xlim(yaxxlim)
        
        def on_ylims_change(event_ax): #changes the limits of the y dendrogram when the heatmap is zoomed
            heatylim = event_ax.get_ylim()
            xaxylim = (10 * heatylim[0], 10 * heatylim[1])
            parent.canvas['heatmap'].figure.axes[0].set_ylim(xaxylim)
        
        parent.canvas[currplt].figure.axes[2].callbacks.connect('xlim_changed', on_xlims_change)
        parent.canvas[currplt].figure.axes[2].callbacks.connect('ylim_changed', on_ylims_change)
        parent.canvas[currplt].figure.axes[2].set_picker(True)
        parent.canvas[currplt].figure.canvas.mpl_connect('pick_event', onpick8)
        parent.fig[currplt].subplots_adjust(left=0.015,right=0.986,
                    bottom=0.271,top=0.975,
                    hspace=0.005,wspace=0.005)
        #parent.canvas[currplt].figure.axes[2].set_xlabel('Sample',  **self.fcsfont)
        parent.canvas[currplt].figure.axes[2].set_ylabel('Feature',  **self.fcsfont)
        parent.canvas[currplt].figure.axes[3].set_aspect(2.5)
        parent.canvas[currplt].figure.axes[2].get_yaxis().set_ticks([])
        parent.canvas[currplt].draw()
        
    def reset(self, parent, currplt, frame, file):
        #makes new figure with updated heatmap and saves
        msdata = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = [2], index_col = [0]).iloc[:,2:]
        cm2 = sns.clustermap(msdata, standard_scale=0, metric="euclidean", method="ward", cmap = parent.analysis_paramsgui.colorscheme) #viridis
        parent.cmind = cm2.dendrogram_row.reordered_ind
        updatedfig = cm2.fig
        parent.canvas[currplt].figure.clf()
            
        figaxes = {} #removes original heatmap components sequentially
        for x in reversed(range(0,4)):
            figaxes[x] = updatedfig.axes[x]
            updatedfig.axes[x].remove()
        for x in range(0,4): # readds new heatmap components sequentially
            figaxes[x].figure=parent.canvas[currplt].figure
            parent.canvas[currplt].figure.axes.append(figaxes[x])
            parent.canvas[currplt].figure.add_subplot(figaxes[x])
        parent.fig[currplt].subplots_adjust(left=0.014,right=0.967,
                    bottom=0.328,top=0.806,
                    hspace=0.005,wspace=0.005)
        parent.highlight[currplt], = parent.canvas[currplt].figure.axes[2].plot([], [], color='yellow', linestyle='-', linewidth=1)
        
        def onpick8(event):
            iondict = pd.read_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
            coord = [event.mouseevent.xdata,event.mouseevent.ydata]
            parent.heatind = int(np.floor(coord[1]))
            name = msdata.index.tolist()[parent.cmind[parent.heatind]]    
    
            parent.ui.lbl_featurename.setText('Compound: ' + name)
            parent.ui.lbl_featurert.setText('Retention time: ' + str(iondict.loc[name,'Retention time (min)']))
            parent.ui.lbl_featuremz.setText('m/z: ' + str(iondict.loc[name,'m/z']))
            parent.highlight_feature(name)
 
        def on_xlims_change(event_ax):#make it soi can use these methods in the first call befre regeneration
            heatxlim = event_ax.get_xlim()
            yaxxlim = (10 * heatxlim[0], 10 * heatxlim[1])
            parent.canvas['heatmap'].figure.axes[1].set_xlim(yaxxlim)
    
        def on_ylims_change(event_ax):
            heatylim = event_ax.get_ylim()
            xaxylim = (10 * heatylim[0], 10 * heatylim[1])
            parent.canvas['heatmap'].figure.axes[0].set_ylim(xaxylim)
        """
        def onresize(event): # i have no idea why this is getting automatically sized back down
            newsize = parent.canvas[currplt].figure.get_size_inches()
            resizeratio = ([newsize[0]/self.figsize[0], newsize[1]/self.figsize[1]])
            self.figsize = parent.canvas[currplt].figure.get_size_inches()
            parent.fig[currplt].subplots_adjust(left=0.014,right=0.967*resizeratio[0],
                                                bottom=0.328,top=0.806*resizeratio[1],
                                                hspace=0.005,wspace=0.005)
            parent.canvas[currplt].draw()
        """
        #parent.canvas[currplt].figure.canvas.mpl_connect('resize_event', onresize)
        parent.canvas[currplt].figure.axes[2].callbacks.connect('xlim_changed', on_xlims_change)
        parent.canvas[currplt].figure.axes[2].callbacks.connect('xlim_changed', on_xlims_change)
        parent.canvas[currplt].figure.axes[2].callbacks.connect('ylim_changed', on_ylims_change)
        parent.canvas[currplt].figure.axes[2].set_picker(True)
        parent.canvas[currplt].figure.canvas.mpl_connect('pick_event', onpick8)
        
        parent.canvas[currplt].figure.set_facecolor(self.plotbackground)
        #parent.canvas[currplt].figure.axes[2].set_xlabel('Sample',  **self.fcsfont)
        parent.canvas[currplt].figure.axes[2].set_ylabel('Feature',  **self.fcsfont)
        parent.canvas[currplt].figure.axes[3].set_aspect(2.5)
        parent.canvas[currplt].figure.axes[2].get_yaxis().set_ticks([])
        self.figsize = parent.canvas[currplt].figure.get_size_inches()
        parent.canvas[currplt].draw()

class plot_mzrt(ui_plot): #feature mass vs retention time plot
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)
        
    def plot(self, parent, file, filtereddfs, groupsets): # abundance tied opacity used here currently
        iondict = pd.read_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = None)
        for elem in filtereddfs:
            if parent.analysis_paramsgui.blnkfltr:
                filtereddfs[elem] = filtereddfs[elem][filtereddfs[elem]['pass_blnkfil']]
            plotcol = groupsets[elem].plotcol.lstrip('#')
            rgbcol = tuple(float(int(plotcol[i:i+2], 16)/255) for i in (0, 2, 4)) #prob need to clean this ups to not use float(int)
            rgbacol = np.asarray([(rgbcol[0], rgbcol[1], rgbcol[2], a) for a in filtereddfs[elem]['logmax']/parent.analysis_paramsgui.maxval])
            rgbacol = np.clip(rgbacol, 0, 1)
            parent.ax[self.currplt].scatter(filtereddfs[elem]['Retention time (min)'].to_list(), filtereddfs[elem]['m/z'].to_list(), c = rgbacol, label = str(groupsets[elem].legendname), picker=True) 
            #parent.ax[self.currplt].scatter(filtereddfs[elem]['Retention time (min)'].to_list(), filtereddfs[elem]['m/z'].to_list(), color = str(groupsets[elem].plotcol), label = str(groupsets[elem].legendname), picker=True, alpha=.5)
        parent.highlight[self.currplt], = parent.ax[self.currplt].plot([], [], 'o', markersize=12, color='yellow')
        parent.ax[self.currplt].set_xlabel("Retention time (min)",  **self.fcsfont)
        parent.ax[self.currplt].set_ylabel('m/z',  **self.fcsfont)
        parent.ax[self.currplt].set_xlim(-.5, 11.5)
        parent.ax[self.currplt].set_ylim(0, 1850)
        parent.ax[self.currplt].legend()
        parent.canvas[self.currplt].figure.canvas.mpl_connect('pick_event', lambda event: self.onpick(event, parent, iondict, ('Retention time (min)', 'm/z')))
        parent.fig[self.currplt].subplots_adjust(left=.1,right=.95,
                            bottom=0.15,top=0.9,
                            hspace=0.2,wspace=0.2)
        parent.canvas[self.currplt].draw() 

class plot_samplecorr(ui_plot): # sample spearman/pearson corelation plot generation
                # need to add option to change correlation type
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)
        
    def plot(self, parent, file, filtereddfs, groupsets):
        iondict = pd.read_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = None)
        msdata = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = [0, 1, 2], index_col = [0, 1, 2])
        msdata = msdata.stack([0,1,2])
        msdata = msdata.groupby(level = [0,1,2,3,4]).mean()
        msdata = msdata.droplevel(level = 3, axis=0)
        msdata = msdata.unstack()
        msdata.index = msdata.index.droplevel([1,2])
        pmatrix = msdata.corr(method='spearman')

        if len(parent.ax[self.currplt].figure.axes)>1:
            sns.heatmap(pmatrix, ax = parent.ax[self.currplt].figure.axes[0], cbar_ax = parent.ax[self.currplt].figure.axes[1], cmap=parent.analysis_paramsgui.colorscheme, vmin=0, vmax=1) #viridis
        else:
            sns.heatmap(pmatrix, ax = parent.ax[self.currplt], cmap=parent.analysis_paramsgui.colorscheme, vmin=0, vmax=1) #viridis
        parent.ax[self.currplt].axes.get_xaxis().get_label().set_visible(False)
        parent.ax[self.currplt].axes.get_yaxis().get_label().set_visible(False)

        parent.fig[self.currplt].subplots_adjust(left=.1,right=.95,
                            bottom=0.15,top=0.9,
                            hspace=0.2,wspace=0.2)
        parent.canvas[self.currplt].draw() 
       
    
class kendrick(ui_plot): #plots mass defect vs nominal mass
                #need to change method name since this isnt actually kendrick mass but just mass defect
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)

    def plot(self, parent, file, filtereddfs, groupsets): #currently uses opacity tied to abundance.
        iondict = pd.read_csv(file, sep = ',', header = [0], index_col = None)
        for elem in filtereddfs:
            if parent.analysis_paramsgui.blnkfltr: #does this need to be here? may be redundant
                filtereddfs[elem] = filtereddfs[elem][filtereddfs[elem]['pass_blnkfil']]

            plotcol = groupsets[elem].plotcol.lstrip('#')
            rgbcol = tuple(float(int(plotcol[i:i+2], 16)/255) for i in (0, 2, 4)) #prob nee to clean this ups to not use float(int)
            rgbacol = np.asarray([(rgbcol[0], rgbcol[1], rgbcol[2], a) for a in filtereddfs[elem]['logmax']/parent.analysis_paramsgui.maxval])
            rgbacol = np.clip(rgbacol, 0, 1)
            parent.ax[self.currplt].scatter(filtereddfs[elem]['m/z'], filtereddfs[elem]['kmd'], c = rgbacol, label = str(groupsets[elem].legendname), picker=True) 
            #parent.ax[self.currplt].scatter(filtereddfs[elem]['m/z'], filtereddfs[elem]['kmd'], color = str(groupsets[elem].plotcol), label = str(groupsets[elem].legendname), picker=True, alpha=.5) 
        parent.highlight[self.currplt], = parent.ax[self.currplt].plot([], [], 'o', markersize=12, color='yellow')
        parent.ax[self.currplt].set_xlabel("m/z",  **self.fcsfont)
        parent.ax[self.currplt].set_ylabel('Mass Defect',  **self.fcsfont)
        parent.ax[self.currplt].set_ylim(0, 1)
        parent.ax[self.currplt].grid()
        parent.ax[self.currplt].legend()
        parent.canvas[self.currplt].figure.canvas.mpl_connect('pick_event', lambda event: self.onpick(event, parent, iondict, ('m/z', 'kmd')))
        parent.fig[self.currplt].subplots_adjust(left=.1,right=.95,
                            bottom=0.15,top=0.9,
                            hspace=0.2,wspace=0.2)
        parent.canvas[self.currplt].draw() 
        
        if parent.analysis_paramsgui.mdguide:
            parent.ax[self.currplt].plot([0, 733.314], [0.00112, 0.8408], color='dimgrey', linestyle='-', linewidth=1)
            parent.ax[self.currplt].plot([63.6623, 733.314], [1, 0.8408], color='dimgrey', linestyle='-', linewidth=1)
            parent.ax[self.currplt].plot([0, 465.456], [0.9884, 0.5408], color='dimgrey', linestyle='-', linewidth=1)

class plot_volcano(ui_plot): # volcano plot of -log10p vs log2 abundance value
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)

    def plot(self, parent, file, filtereddfs, groupsets):
        pqvar = '-logq'
        if parent.analysis_paramsgui.FDR:
            parent.ui.lbl_volcanowarn.setText('')
        else:
            parent.ui.lbl_volcanowarn.setText('False discovery rate correction off')
            pqvar = '-logp'
            
        querylist = parent.analysis_paramsgui.querylist
        iondict = pd.read_csv(file, sep = ',', header = [0], index_col = None)
        

        for elem in querylist:
            if parent.analysis_paramsgui.blnkfltr: #this uses ionfilter object which may be deprecated long term, see comments on this class in stats module
                filtereddfs[elem] = filtereddfs[elem][filtereddfs[elem]['pass_blnkfil']]#check why this gets called in conditional? should be true if blankfil is off, does this even need to be here if these are already filtered?
            filtereddfs[elem] = listfilter(iondict, groupsets[elem].ionlist, True)
            filtereddfs[elem]['logfc'] = np.log2(filtereddfs[elem]['fc']) #not sure if best to move this bit to stats?
        iondict['logfc'] = np.log2(iondict['fc'])
        iondict.to_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', header = True, index = False)

        maxpval = 0
        for elem in filtereddfs: 
            if parent.analysis_paramsgui.blnkfltr: 
                filtereddfs[elem] = filtereddfs[elem][filtereddfs[elem]['pass_blnkfil']] 
            if filtereddfs[elem][pqvar].max() > maxpval:
                maxpval = filtereddfs[elem][pqvar].max()
            sig = filtereddfs[elem][filtereddfs[elem][pqvar] >= -np.log10(parent.analysis_paramsgui.pqthresh)]
            sig = sig[sig['logfc'].abs() >= np.log2(parent.analysis_paramsgui.fcthresh)] 
            nonsig = filtereddfs[elem][~filtereddfs[elem]['Compound'].isin(sig['Compound'].to_list())]
            parent.ax[self.currplt].scatter(sig[sig['logfc'] > 0]['logfc'], sig[sig['logfc'] > 0][pqvar], color = 'red', picker=True, alpha=0.5)
            parent.ax[self.currplt].scatter(sig[sig['logfc'] <= 0]['logfc'], sig[sig['logfc'] <= 0][pqvar], color = 'blue', picker=True, alpha=0.5)
            parent.ax[self.currplt].scatter(nonsig['logfc'], nonsig[pqvar], color = 'black', picker=True, alpha=0.5)
            
        parent.highlight[self.currplt], = parent.ax[self.currplt].plot([], [], 'o', markersize=12, color='yellow')
        parent.ax[self.currplt].plot([-np.log2(parent.analysis_paramsgui.fcthresh), -np.log2(parent.analysis_paramsgui.fcthresh)], [0, maxpval*1.2], color='dimgrey', linestyle='-', linewidth=1)
        parent.ax[self.currplt].plot([np.log2(parent.analysis_paramsgui.fcthresh), np.log2(parent.analysis_paramsgui.fcthresh)], [0, maxpval*1.2], color='dimgrey', linestyle='-', linewidth=1)
        parent.ax[self.currplt].plot([-6.75, 6.75], [-np.log10(parent.analysis_paramsgui.pqthresh), -np.log10(parent.analysis_paramsgui.pqthresh)], color='dimgrey', linestyle='-', linewidth=1)
        parent.ax[self.currplt].set_xlabel("log2 fold change",  **self.fcsfont) #"$Log_2$" is code for subscript but is ital?
        parent.ax[self.currplt].set_ylabel('-log10 '+pqvar[-1]+'-value',  **self.fcsfont)
        parent.ax[self.currplt].set_xlim(-6.75, 6.75)
        try:
            parent.ax[self.currplt].set_ylim(0, maxpval*1.1)
        except Exception:
            self.error('Warning: No volcano plot features generated, check test groups')
            pass
        parent.ax[self.currplt].grid()
        parent.canvas[self.currplt].figure.canvas.mpl_connect('pick_event', lambda event: self.onpick(event, parent, iondict, ('logfc', '-logq')))
        parent.fig[self.currplt].subplots_adjust(left=.1,right=.95,
                            bottom=0.15,top=0.9,
                            hspace=0.2,wspace=0.2)
        parent.canvas[self.currplt].draw()
 
class plot_fc3d(ui_plot):   # 3d mass, retention time, fold change plot, not currently highlightable
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)

    def plot(self, parent, file, filtereddfs, groupsets): 
        iondict = pd.read_csv(file, sep = ',', header = [0], index_col = None)
        for elem in parent.analysis_paramsgui.querylist:
            if parent.analysis_paramsgui.blnkfltr:
                filtereddfs[elem] = filtereddfs[elem][filtereddfs[elem]['pass_blnkfil']] # check why this is here
            filtereddfs[elem] = listfilter(iondict, groupsets[elem].ionlist, True)
            filtereddfs[elem]['logfc'] = np.log2(filtereddfs[elem]['fc'])#dothis inthe main function
        
        parent.ax[self.currplt].remove()
        parent.ax[self.currplt] = parent.canvas[self.currplt].figure.add_subplot(111, projection='3d')
        parent.ax[self.currplt].set_axisbelow(True)
        for elem in filtereddfs:
            x = filtereddfs[elem]['logfc']
            z = filtereddfs[elem]['m/z']
            y = filtereddfs[elem]['Retention time (min)']
            parent.ax[self.currplt].scatter(x, y, z, color = str(groupsets[elem].plotcol), marker='o', label = str(groupsets[elem].legendname))    
        parent.canvas[self.currplt].figure.set_facecolor(self.plotbackground)
        parent.ax[self.currplt].set_facecolor(self.plotbackground)
        parent.ax[self.currplt].set_xlabel('log2 fold change',  **self.fcsfont, labelpad=20)
        parent.ax[self.currplt].set_ylabel('Retention time (min)',  **self.fcsfont, labelpad=20)
        parent.ax[self.currplt].set_zlabel('m/z',  **self.fcsfont, labelpad=25)
        parent.ax[self.currplt].tick_params(axis='z', pad=10)
        parent.ax[self.currplt].set_ylim(-.5, 11.5)
        parent.ax[self.currplt].grid()
        parent.ax[self.currplt].legend()
        parent.fig[self.currplt].subplots_adjust(left=.1,right=.95,
                            bottom=0.15,top=0.9,
                            hspace=0.2,wspace=0.2)
        parent.canvas[self.currplt].draw()

class plot_dendrogram(ui_plot): # dendrogram generation
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)
    
    def plot(self, parent, file, filtereddfs, groupsets):
        heirarch = pd.read_csv(file, sep = ',', header = [2], index_col = [0]).drop(['m/z', 'Retention time (min)'], axis=1)
        data_scaled = normalize(heirarch, axis = 0) #normalize features
        data_scaled = pd.DataFrame(data_scaled, columns=heirarch.columns, index=heirarch.index)
        textlabels = []
        for elem in data_scaled.columns.tolist(): #to cut off dates, probably exclude this in final release
            #textlabels.append(elem[7:])
            textlabels.append(elem)
            
        if parent.analysis_paramsgui.bootstrap:
            #bootstrap dendrogram
            pv = PvClust(data_scaled, method="ward", metric="euclidean", nboot=1000,
                         parallel=False)
            dend = pv.plot(parent.ax[self.currplt], labels = textlabels)
        else:
            #regular dendrogram
            dend = shc.dendrogram(shc.linkage(data_scaled.transpose(), method='ward'), ax = parent.ax[self.currplt], leaf_rotation=90, color_threshold=0, above_threshold_color = 'black', labels = textlabels) #default leaf label size 16
        
        parent.fig[self.currplt].subplots_adjust(left=.1,right=.95,
                            bottom=0.35,top=0.9,
                            hspace=0.2,wspace=0.2)
        parent.canvas[self.currplt].draw()

class plot_PCA(ui_plot): #plots NMDS data
        # should include opion to allow user specified pca colors
        # need to fix selection of samples on PCA plot
        # should add PCA vs NMDS option
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)
        
    def plot(self, parent, file, filtereddfs, groupsets):
        parent.collapsereps = parent.dialog.ui.checkBox_collapsereps.isChecked()
        if parent.collapsereps: #if replicate collapse is selected average techreps
            msdata = pd.read_csv(file, sep = ',', header = [0, 1, 2], index_col = [0, 1, 2]) #imports data
            msdata = msdata.stack([0,1,2]) #following has to do some header reformatting
            msdata =  msdata.groupby(level = [0,1,2,3,4]).mean().unstack(level = [-1,-2])
            test2 =msdata.columns.to_list()
            msdata = msdata.reset_index()
            header = [('','','Compound'), ('','','m/z'), ('','','Retention time (min)')]
            for elem in test2: #rename test2
                header.append((elem[1], '', elem[0]))
            msdata.columns = pd.MultiIndex.from_tuples(header)
            msdata.to_csv('averagepca.csv', header = True, index = False)
        
            msdata_header = pd.read_csv('averagepca.csv', sep = ',', header = None, index_col = [0,1,2]).iloc[:3,:].transpose()
            pcadf = pd.read_csv('averagepca.csv', sep = ',', header = [2], index_col = [0]).drop(['m/z', 'Retention time (min)'], axis=1).transpose().astype(float).reset_index().rename(columns={'index': 'File'})### added astype float to work with integer measurement data
        else:
            msdata_header = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = None, index_col = [0,1,2]).iloc[:3,:].transpose() 
            pcadf = pd.read_csv(file, sep = ',', header = [2], index_col = [0]).drop(['m/z', 'Retention time (min)'], axis=1).transpose().astype(float).reset_index().rename(columns={'index': 'File'}) #### added astype float to work with integer measurement data

        components = len(msdata_header.index)
        if components > 10:
            components = 10
        msdata_header.columns = ['Biolgroup', 'Sample', 'Injection'] #could clean up this section for color assignment
        msdata_header = msdata_header.set_index('Injection')
        colors, colorpos, biolgroupmap = ['red','blue','black','grey','purple','orange','green','yellow','lime', 'plum', 'teal', 'olivedrab', 'sienna', 'maroon', 'navy'], 0, {}
        for elem in msdata_header['Biolgroup']:
            if elem not in biolgroupmap and elem != parent.analysis_paramsgui.blnkgrp: ###### delete blank clause OR CHANGE TO THE BLNKFILTER OPTION
                biolgroupmap[elem] = colors[colorpos]
                colorpos += 1
        
        features = list(pcadf.columns.values)[1:]
        x = pcadf.loc[:, features].values
        y = pcadf.loc[:,['File']].values
        x -= x.mean()#.astype(int) #remove this!!!!astypent this was need to prevent trowing anerror with bruker data
        similarities = pairwise_distances(x, metric='braycurtis')
    
        mds = manifold.MDS(n_components=components, max_iter=3000, eps=1e-9, random_state=1,
                   dissimilarity="precomputed", n_jobs=1)
        pos = mds.fit(similarities).embedding_
        
        nmds = manifold.MDS(n_components=components, metric=False, max_iter=3000, eps=1e-12,
                    dissimilarity="precomputed", random_state=1, n_jobs=1,
                    n_init=1)
        npos = nmds.fit_transform(similarities, init=pos)

        pca = PCA(n_components = components)
        nmdspc = pca.fit_transform(npos)
        expvar = pca.explained_variance_ratio_
        pcadftest = pd.DataFrame(data = nmdspc)

        ncomplist = []
        for elem in range(0,components):
            ncomplist.append(elem)
        nmdspc = pd.DataFrame(data = nmdspc, columns = ncomplist)
        nmdspc['File'] = pcadf['File']
        pos, samplesdone =0, []
        nmdspc['Biolgroup'] = ''
        for elem in nmdspc.iloc[:, components]:
            nmdspc.iloc[pos, components + 1] = msdata_header.loc[elem, 'Biolgroup']
            pos+=1
        principalDf = nmdspc.set_index('File')
                
        for elem in biolgroupmap:
            scatterframe = principalDf[principalDf['Biolgroup'] == elem]
            points = scatterframe.iloc[:,[0,1]].to_numpy() #not sure why i cant use.loc for this block, throws index not found error? used to use x and y.
            if np.shape(points)[0] > 2:
                self.plot_point_cov(points, nstd=2, ax = parent.ax[self.currplt], alpha=0.5, color = self.lighten_color(biolgroupmap[elem], 0.3))
            parent.ax[self.currplt].scatter(scatterframe.iloc[:,0], scatterframe.iloc[:,1], color = biolgroupmap[elem], marker='o', s = 30, label = str(elem), picker=True)
        parent.highlight[self.currplt], = parent.ax[self.currplt].plot([], [], 'o', markersize=12, color='yellow')
        parent.ax[self.currplt].set_xlabel('NMDS1',  **self.fcsfont) # (' + str(round(100*expvar[0], 2)) + '%)'
        parent.ax[self.currplt].set_ylabel('NMDS2',  **self.fcsfont) #(' + str(round(100*expvar[1], 2)) + '%)'
        
        #following two lines put a hard limit on the axis tick distance
        #parent.ax[self.currplt].xaxis.set_major_locator(ticker.MultipleLocator(0.1))
        #parent.ax[self.currplt].yaxis.set_major_locator(ticker.MultipleLocator(0.1))
        
        def picksample(event): #fixthis
            ind = event.ind
            coord = event.artist.get_offsets()[ind,:]
            parent.pickedsample = principalDf.loc[principalDf['0'] == coord[0,0], :].loc[principalDf['1'] == coord[0,1], :].reset_index()
            parent.ui.lbl_injname.setText('Injection/Sample: ' + str(parent.pickedsample.iloc[0,0]))
            parent.highlight[self.currplt].set_data(coord[0,0],coord[0,1])
            parent.canvas[self.currplt].draw_idle()
            
        parent.canvas[self.currplt].figure.canvas.mpl_connect('pick_event', picksample)
        parent.fig[self.currplt].subplots_adjust(left=.1,right=.9,
                            bottom=0.1,top=0.9,
                            hspace=0.2,wspace=0.2)
        #x0,x1 = parent.ax[self.currplt].get_xlim()
        #0,y1 = parent.ax[self.currplt].get_ylim()
        #parent.ax[self.currplt].set_aspect(abs(x1-x0)/abs(y1-y0))
        #parent.ax[self.currplt].set_aspect('equal')
        parent.ax[self.currplt].legend()
        parent.canvas[self.currplt].draw()
    
        #following handles confidence interval generation
    def plot_point_cov(self, points, nstd=2, ax=None, **kwargs): #gets point values
        pos = points.mean(axis=0)
        cov = np.cov(points, rowvar=False)
        return self.plot_cov_ellipse(cov, pos, nstd, ax, **kwargs)
    
    def lighten_color(self, color, amount=0.5): #lightens color of ellipse by 50%
        import matplotlib.colors as mc
        import colorsys
        try:
            c = mc.cnames[color]
        except:
            c = color
        c = colorsys.rgb_to_hls(*mc.to_rgb(c))
        return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
    
    def plot_cov_ellipse(self, cov, pos, nstd=2, ax=None, **kwargs): #generatates optimized ellipse
        
        def eigsorted(cov):
            vals, vecs = np.linalg.eigh(cov)
            order = vals.argsort()[::-1]
            return vals[order], vecs[:,order]
    
        if ax is None:
            ax = plt.gca()
            
        vals, vecs = eigsorted(cov)
        theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
        width, height = 2 * nstd * np.sqrt(vals)
        ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, **kwargs)
        ax.add_artist(ellip)
        return ellip
 
class prev_cv(ui_plot): # CV rarifactions plot with mean and median CV
    def __init__(self, parent, currplt, frame, file, filtereddfs, groupsets):
        ui_plot.__init__(self, parent, currplt, frame)
        self.parent = parent
        self.currplt = currplt
        self.plot(parent, file, filtereddfs, groupsets)
        
    def plot(self, parent, file, filtereddfs, groupsets):
        # sorts and saves mean and median CV DFs
        iondict = pd.read_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', header = [0], index_col = [0])
        iondict = iondict[~np.isnan(iondict['average CV'])]
        iondictmean = iondict.sort_values(['average CV'], ascending=[1]).reset_index()
        iondictmed = iondict.sort_values(['median CV'], ascending=[1]).reset_index()
        iondictmean = iondictmean.reset_index()
        iondictmed = iondictmed.reset_index()
        iondictmean.iloc[:,0] = 100 * iondictmean.iloc[:,0]/len(iondictmean['average CV'])
        iondictmed.iloc[:,0] = 100 * iondictmed.iloc[:,0]/len(iondictmed['median CV'])
    
        # Calculates maximum theoretical CV based on neff, maybe change to just use max value, not sure
        msdata_header = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = None, index_col = [0,1,2]).iloc[:3,:].transpose()
        msdata_header.columns = ['Biolgroup', 'Sample', 'Injection']
        iondict_sorted = iondictmean
        average_n = msdata_header['Injection'].nunique()/msdata_header['Sample'].nunique()
        modelstdevlist = [1]
        for num in range(1, int(average_n)):
            modelstdevlist.append(0)
        modelstdev = pd.Series(modelstdevlist).std()/pd.Series(modelstdevlist).mean()
        cv50 = iondict_sorted.iloc[(iondict_sorted.iloc[:,0]-50).abs().argsort()[:1]]['average CV']
        qualscore = float(round(100*(1-cv50/modelstdev),1)) #generates currently unused quality score
        parent.ui.lbl_spllist_3.setText('Overall: ' + str(qualscore)  + '%')
        
        currplt = 'cvplt' #instead take this from input
        parent.ax[currplt].plot(iondictmed['median CV'], iondictmed.iloc[:,0], color = '#0000ff', label="Median CV")
        parent.ax[currplt].plot(iondictmean['average CV'], iondictmed.iloc[:,0], color = 'red', label="Mean CV")
        parent.ax[currplt].set_xlabel("CV",  **self.fcsfont)
        parent.ax[currplt].set_ylabel('Percentage of Features',  **self.fcsfont)
        parent.ax[currplt].legend()
        parent.ax[currplt].set_xlim([0, modelstdev])
        parent.ax[currplt].set_ylim([0, 100])
        parent.ax[currplt].plot([parent.analysis_paramsgui.cvthresh, parent.analysis_paramsgui.cvthresh], [0, 100], color='dimgrey', linestyle='-', linewidth=1)
        threshpercent = iondictmed.iloc[(iondictmed[parent.analysis_paramsgui.cvparam]-parent.analysis_paramsgui.cvthresh).abs().argsort()[:1],0]
        parent.ax[currplt].plot([0, modelstdev], [threshpercent, threshpercent] , color='dimgrey', linestyle='-', linewidth=1)
            
        
        parent.fig[currplt].subplots_adjust(left=.15,right=0.9,
                            bottom=.15,top=.85,
                            hspace=10,wspace=10)
        parent.canvas[currplt].draw()
    
def gen_upsetplt(parent): #upset plot to visualize sets of compounds in groups
        #need to do something to handle groups with names that are substrings of other group names
    iondict = pd.read_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = None)
    if parent.analysis_paramsgui.relfil:
        iondict = iondict[iondict['pass_relfil']]
    if parent.analysis_paramsgui.decon:
        iondict = iondict[iondict['pass_insource']]
    if parent.analysis_paramsgui.blnkfltr:
        iondict = iondict[iondict['pass_blnkfil']]
    if parent.analysis_paramsgui.CVfil:
        iondict = iondict[iondict['pass_cvfil']]
    iongroups = iondict['groups'].to_list()
    freq, biolgroups, sets = {}, [], []
    for item in iongroups: 
        if (item not in freq): 
            freq[item] = 0
        freq[item] += 1
    
    header = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = None, index_col = [0,1,2]).iloc[0,:]
    for elem in header:
        if elem not in biolgroups:
            biolgroups.append(elem)
    
    for elem in list(freq.keys()): #have to do this if one group is a substring of another, add space
        sets.append(' ' + elem)
    size = list(freq.values())
    setdf = pd.DataFrame({'groups':sets})
    for elem in biolgroups:
        setdf[elem] = setdf['groups'].str.contains(' ' + elem)
    setdf['size'] = size
    setdf = setdf.iloc[:,1:]
    setdf = setdf.set_index(biolgroups)['size']
    
    with plt.rc_context({"font.size"   : 8}):
        upsetplt = upsetplot.plot(setdf, show_counts='%d', show_percentages=True, sort_categories_by=None)
    figup = upsetplt['matrix'].figure
    figup.set_size_inches(5, 4)
    #upsetplt['matrix'].yaxis.tick_right()
    figup.set_facecolor((0,0,0,0))
    upsetplt['intersections'].set_facecolor((1,1,1,.25))
    figup.savefig('test_upsetplt.png', dpi=150, bbox_inches='tight')
    pixmap = QPixmap('test_upsetplt.png')
    parent.ui.label_upset.setPixmap(pixmap)
    
def gen_treemap(parent): #generate treemap for visualization of filtering levels
        #needed to refilter data and see how df row lengths change to avoid issues with one feature being in multiple filter lists
    plt.clf()
    msdata_filtered = pd.read_csv(parent.analysis_paramsgui.outputdir / (parent.analysis_paramsgui.filename.stem + '_filtered.csv'), sep = ',', header = [0, 1, 2], index_col = [0, 1, 2])#need to change this to get original file...
    fltrcnt, color = {}, []
    iondict = pd.read_csv(parent.analysis_paramsgui.outputdir / 'iondict.csv', sep = ',', header = [0], index_col = [0])
    total = len(iondict.index)
    current = total
    if parent.analysis_paramsgui.relfil:
        filteredsetsize = len(iondict[iondict['pass_relfil']].index)
        fltrcnt['Mispicked'] = current - filteredsetsize
        current = filteredsetsize
        color.append('#0000ff')
    if parent.analysis_paramsgui.blnkfltr:
        filteredsetsize = len(iondict[iondict['pass_blnkfil']].index)
        fltrcnt['Blank'] = current - filteredsetsize
        current = filteredsetsize
        color.append('#00aaaa')
    if parent.analysis_paramsgui.CVfil:#needed to use ionlist instead of filtering down like others, not sure why
        fltrcnt['Nonreproducible'] = len(parent.ionfilters['cv'].ions)
        current = current - fltrcnt['Nonreproducible']
        color.append('#ff0000')
    if parent.analysis_paramsgui.decon: #this only works if the deconvolution is done on the filtered dataset, not unfiltered!
        fltrcnt['Insource'] = len(parent.ionfilters['insource'].ions)
        color.append('#00aa00')
    fltrcnt['High Quality'] = len(msdata_filtered.index)
    color.append('#000000')

    sizes=list(fltrcnt.values())
    totalsize = sum(fltrcnt.values())
    label=list(fltrcnt.keys())
    for pos in range(0,len(label)):
        label[pos] = label[pos] + '\n' + str(sizes[pos]) + '\n' + str(round(100*sizes[pos]/totalsize,1)) + '%'
    squarify.plot(sizes=sizes, label=label, color=color, alpha=0.3, text_kwargs={'fontsize':10})
    plt.axis('off')
    plt.savefig('treemap.png', dpi=150, bbox_inches='tight')
    pixmap = QPixmap('treemap.png')
    parent.ui.label_treemap.setPixmap(pixmap)