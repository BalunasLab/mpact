"""
MPACT
Copyright 2022, Robert M. Samples, Sara P. Puckett, and Marcy J. Balunas
"""

import sys
from PyQt5 import QtSvg
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) 
svgWidget = QtSvg.QSvgWidget('1.svg')
svgWidget.show()

sys.exit(app.exec_())
