# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plotparam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.centralwidget)
        self.title_bar.setMinimumSize(QtCore.QSize(0, 50))
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setLineWidth(1)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setStyleSheet("background-color: rgb(40, 40, 40)\n"
"")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setLineWidth(0)
        self.frame_title.setObjectName("frame_title")
        self._3 = QtWidgets.QVBoxLayout(self.frame_title)
        self._3.setContentsMargins(15, 0, 0, 0)
        self._3.setSpacing(0)
        self._3.setObjectName("_3")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_title)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_top_btns.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_top_btns.setStyleSheet("background-color: rgba(33, 37, 43, 150);")
        self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"margin-left: 5px;")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_13.addWidget(self.label_title_bar_top)
        self.horizontalLayout_12.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_btns_right.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons/16x16/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_14.addWidget(self.btn_close)
        self.horizontalLayout_12.addWidget(self.frame_btns_right)
        self._3.addWidget(self.frame_top_btns)
        self.horizontalLayout_3.addWidget(self.frame_title)
        self.verticalLayout.addWidget(self.title_bar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_plotparams = QtWidgets.QFrame(self.page)
        self.frame_plotparams.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(34, 34, 34, 255), stop:1 rgba(52, 52, 52, 255));")
        self.frame_plotparams.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plotparams.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plotparams.setObjectName("frame_plotparams")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_plotparams)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.frame_plotparams)
        self.frame_3.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_applyfilter = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_applyfilter.setMinimumSize(QtCore.QSize(0, 40))
        self.checkBox_applyfilter.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox_applyfilter.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_applyfilter.setFont(font)
        self.checkBox_applyfilter.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
"    background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 24px;\n"
"     height: 24px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"   image: url(:/resources/icons/24x24/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"   image: url(:/resources/icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_applyfilter.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_applyfilter.setCheckable(True)
        self.checkBox_applyfilter.setChecked(True)
        self.checkBox_applyfilter.setObjectName("checkBox_applyfilter")
        self.verticalLayout_4.addWidget(self.checkBox_applyfilter)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_bootstrap = QtWidgets.QFrame(self.frame_plotparams)
        self.frame_bootstrap.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_bootstrap.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_bootstrap.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_bootstrap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bootstrap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bootstrap.setObjectName("frame_bootstrap")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_bootstrap)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkBox_bootstrap = QtWidgets.QCheckBox(self.frame_bootstrap)
        self.checkBox_bootstrap.setMinimumSize(QtCore.QSize(0, 40))
        self.checkBox_bootstrap.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox_bootstrap.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_bootstrap.setFont(font)
        self.checkBox_bootstrap.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
"    background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 24px;\n"
"     height: 24px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"   image: url(:/resources/icons/24x24/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"   image: url(:/resources/icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_bootstrap.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_bootstrap.setCheckable(True)
        self.checkBox_bootstrap.setChecked(False)
        self.checkBox_bootstrap.setObjectName("checkBox_bootstrap")
        self.verticalLayout_7.addWidget(self.checkBox_bootstrap)
        self.verticalLayout_6.addWidget(self.frame_bootstrap)
        self.frame_2 = QtWidgets.QFrame(self.frame_plotparams)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_collapsereps = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_collapsereps.setMinimumSize(QtCore.QSize(0, 40))
        self.checkBox_collapsereps.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox_collapsereps.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_collapsereps.setFont(font)
        self.checkBox_collapsereps.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
"    background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 24px;\n"
"     height: 24px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"   image: url(:/resources/icons/24x24/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"   image: url(:/resources/icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_collapsereps.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_collapsereps.setCheckable(True)
        self.checkBox_collapsereps.setChecked(True)
        self.checkBox_collapsereps.setObjectName("checkBox_collapsereps")
        self.verticalLayout_3.addWidget(self.checkBox_collapsereps)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.frame_mdguide = QtWidgets.QFrame(self.frame_plotparams)
        self.frame_mdguide.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_mdguide.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_mdguide.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_mdguide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mdguide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mdguide.setObjectName("frame_mdguide")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_mdguide)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_mdguide = QtWidgets.QCheckBox(self.frame_mdguide)
        self.checkBox_mdguide.setMinimumSize(QtCore.QSize(0, 40))
        self.checkBox_mdguide.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox_mdguide.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_mdguide.setFont(font)
        self.checkBox_mdguide.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
"    background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 24px;\n"
"     height: 24px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"   image: url(:/resources/icons/24x24/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-media-stop.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"   image: url(:/resources/icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources/icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources/icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_mdguide.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_mdguide.setCheckable(True)
        self.checkBox_mdguide.setChecked(True)
        self.checkBox_mdguide.setObjectName("checkBox_mdguide")
        self.verticalLayout_5.addWidget(self.checkBox_mdguide)
        self.verticalLayout_6.addWidget(self.frame_mdguide)
        self.frame_volcanoparams = QtWidgets.QFrame(self.frame_plotparams)
        self.frame_volcanoparams.setMinimumSize(QtCore.QSize(20, 70))
        self.frame_volcanoparams.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_volcanoparams.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_volcanoparams.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_volcanoparams.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_volcanoparams.setObjectName("frame_volcanoparams")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_volcanoparams)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_blankfil_name_2 = QtWidgets.QLabel(self.frame_volcanoparams)
        self.lbl_blankfil_name_2.setMinimumSize(QtCore.QSize(120, 20))
        self.lbl_blankfil_name_2.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_blankfil_name_2.setFont(font)
        self.lbl_blankfil_name_2.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_blankfil_name_2.setObjectName("lbl_blankfil_name_2")
        self.gridLayout.addWidget(self.lbl_blankfil_name_2, 0, 0, 1, 1)
        self.lineEdit_pqthresh = QtWidgets.QLineEdit(self.frame_volcanoparams)
        self.lineEdit_pqthresh.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_pqthresh.setMaximumSize(QtCore.QSize(150, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.lineEdit_pqthresh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_pqthresh.setFont(font)
        self.lineEdit_pqthresh.setStyleSheet("QLineEdit{ \n"
"    background-color:rgba(255,255,255,10);\n"
"    border: 0px solid lightgray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    font-size: 18px;\n"
"    font-family: Bahnschrift SemiBold\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color:rgba(0,0,0,0);\n"
"}")
        self.lineEdit_pqthresh.setObjectName("lineEdit_pqthresh")
        self.gridLayout.addWidget(self.lineEdit_pqthresh, 0, 1, 1, 1)
        self.lineEdit_fcthresh = QtWidgets.QLineEdit(self.frame_volcanoparams)
        self.lineEdit_fcthresh.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_fcthresh.setMaximumSize(QtCore.QSize(150, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.lineEdit_fcthresh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_fcthresh.setFont(font)
        self.lineEdit_fcthresh.setStyleSheet("QLineEdit{ \n"
"    background-color:rgba(255,255,255,10);\n"
"    border: 0px solid lightgray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    font-size: 18px;\n"
"    font-family: Bahnschrift SemiBold\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color:rgba(0,0,0,0);\n"
"}")
        self.lineEdit_fcthresh.setObjectName("lineEdit_fcthresh")
        self.gridLayout.addWidget(self.lineEdit_fcthresh, 1, 1, 1, 1)
        self.lbl_blankfil_name_4 = QtWidgets.QLabel(self.frame_volcanoparams)
        self.lbl_blankfil_name_4.setMinimumSize(QtCore.QSize(120, 20))
        self.lbl_blankfil_name_4.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_blankfil_name_4.setFont(font)
        self.lbl_blankfil_name_4.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_blankfil_name_4.setObjectName("lbl_blankfil_name_4")
        self.gridLayout.addWidget(self.lbl_blankfil_name_4, 1, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_volcanoparams)
        self.frame_colorscheme = QtWidgets.QFrame(self.frame_plotparams)
        self.frame_colorscheme.setMinimumSize(QtCore.QSize(20, 30))
        self.frame_colorscheme.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_colorscheme.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_colorscheme.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_colorscheme.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_colorscheme.setObjectName("frame_colorscheme")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_colorscheme)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_blankfil_name_5 = QtWidgets.QLabel(self.frame_colorscheme)
        self.lbl_blankfil_name_5.setMinimumSize(QtCore.QSize(130, 20))
        self.lbl_blankfil_name_5.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_blankfil_name_5.setFont(font)
        self.lbl_blankfil_name_5.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_blankfil_name_5.setObjectName("lbl_blankfil_name_5")
        self.horizontalLayout_2.addWidget(self.lbl_blankfil_name_5)
        self.combo_colorscheme = QtWidgets.QComboBox(self.frame_colorscheme)
        self.combo_colorscheme.setMinimumSize(QtCore.QSize(140, 30))
        self.combo_colorscheme.setMaximumSize(QtCore.QSize(150, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.combo_colorscheme.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.combo_colorscheme.setFont(font)
        self.combo_colorscheme.setStyleSheet("QComboBox{ \n"
"    background-color:rgba(255,255,255,10);\n"
"    border: 0px solid lightgray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    font-size: 18px;\n"
"    font-family: Bahnschrift SemiBold;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/resources/icons/16x16/cil-chevron-bottom.png)\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 0px solid lightgray;\n"
"    color:  rgb(212, 212, 212);\n"
"    background-color:  rgb(255, 255, 255, 45);\n"
"    selection-background-color:  rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QListView {\n"
"    color: rgb(212, 212, 212);\n"
"    background-color: rgb(40,40,40);\n"
"}")
        self.combo_colorscheme.setEditable(True)
        self.combo_colorscheme.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combo_colorscheme.setObjectName("combo_colorscheme")
        self.combo_colorscheme.addItem("")
        self.combo_colorscheme.addItem("")
        self.combo_colorscheme.addItem("")
        self.combo_colorscheme.addItem("")
        self.combo_colorscheme.addItem("")
        self.combo_colorscheme.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_colorscheme)
        self.verticalLayout_6.addWidget(self.frame_colorscheme)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.frame_plotparams)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setSizeIncrement(QtCore.QSize(0, 40))
        self.frame.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_apply = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_apply.sizePolicy().hasHeightForWidth())
        self.btn_apply.setSizePolicy(sizePolicy)
        self.btn_apply.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_apply.setMaximumSize(QtCore.QSize(150, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_apply.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_apply.setFont(font)
        self.btn_apply.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 57, 57)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/icons/16x16/cil-description.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_apply.setIcon(icon1)
        self.btn_apply.setIconSize(QtCore.QSize(16, 16))
        self.btn_apply.setAutoRepeatDelay(305)
        self.btn_apply.setObjectName("btn_apply")
        self.horizontalLayout.addWidget(self.btn_apply)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_plotparams)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Plot Configuration</span></p></body></html>"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.checkBox_applyfilter.setText(_translate("MainWindow", "Apply Data Filtering"))
        self.checkBox_bootstrap.setText(_translate("MainWindow", "Bootstrap Analysis"))
        self.checkBox_collapsereps.setText(_translate("MainWindow", "Collapse Technical Replicates"))
        self.checkBox_mdguide.setText(_translate("MainWindow", "Mass Defect Guidelines"))
        self.lbl_blankfil_name_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">p/q Threshold</span></p></body></html>"))
        self.lineEdit_pqthresh.setText(_translate("MainWindow", "0.05"))
        self.lineEdit_fcthresh.setText(_translate("MainWindow", "1.5"))
        self.lbl_blankfil_name_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">FC Threshold</span></p></body></html>"))
        self.lbl_blankfil_name_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Color Scheme</span></p></body></html>"))
        self.combo_colorscheme.setItemText(0, _translate("MainWindow", "rocket"))
        self.combo_colorscheme.setItemText(1, _translate("MainWindow", "mako"))
        self.combo_colorscheme.setItemText(2, _translate("MainWindow", "flare"))
        self.combo_colorscheme.setItemText(3, _translate("MainWindow", "crest"))
        self.combo_colorscheme.setItemText(4, _translate("MainWindow", "magma"))
        self.combo_colorscheme.setItemText(5, _translate("MainWindow", "viridis"))
        self.btn_apply.setToolTip(_translate("MainWindow", "Import"))
        self.btn_apply.setText(_translate("MainWindow", "Apply"))

import files_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

