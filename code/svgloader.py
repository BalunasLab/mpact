import sys
from PyQt5 import QtSvg
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) 
svgWidget = QtSvg.QSvgWidget('1.svg')
svgWidget.show()

sys.exit(app.exec_())
