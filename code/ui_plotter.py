"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""


class genfeatureplot:
    
    def __init__(self, name, groupionlists, iondictloc):
        
    def onpick(self, self.main, event):
        ind = event.ind
        coord = event.artist.get_offsets()[ind,:]
        self.main.pickedfeature = iondict.loc[abs(iondict[self.xvar] - coord[0,0]) <= 0.001, :].loc[abs(iondict[self.yvar] - coord[0,1]) <= 0.001, :].reset_index()
        self.main.pickedfeature = str(self.pickedfeature.iloc[0,0])
        self.main.ui.lbl_featurename.setText('Compound: ' + self.main.pickedfeature)
        self.main.ui.lbl_featurert.setText('Retention time: ' + str(round(self.main.pickedfeature, 4)))
        self.main.ui.lbl_featuremz.setText('m/z: ' + str(round(self.main.pickedfeature, 4)))
            
        self.main.highlight_feature()