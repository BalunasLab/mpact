# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Xanadu\Desktop\Project folder\code\ui_featureinfo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 752)
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
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("background-color: rgb(35,35,35)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_sidebar_plot = QtWidgets.QFrame(self.frame_4)
        self.frame_sidebar_plot.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_sidebar_plot.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_sidebar_plot.setStyleSheet("background-color: rgb(35,35,35,0\n"
")")
        self.frame_sidebar_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sidebar_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sidebar_plot.setObjectName("frame_sidebar_plot")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_sidebar_plot)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btn_abund = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_abund.sizePolicy().hasHeightForWidth())
        self.btn_abund.setSizePolicy(sizePolicy)
        self.btn_abund.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_abund.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_abund.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_abund.setFont(font)
        self.btn_abund.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(225,225,225, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(225,225,225, 255);\n"
"    color: rgba(75,75,75,255)\n"
"}")
        self.btn_abund.setAutoRepeatDelay(305)
        self.btn_abund.setObjectName("btn_abund")
        self.verticalLayout_9.addWidget(self.btn_abund)
        self.btn_hits = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_hits.sizePolicy().hasHeightForWidth())
        self.btn_hits.setSizePolicy(sizePolicy)
        self.btn_hits.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_hits.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_hits.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_hits.setFont(font)
        self.btn_hits.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(225,225,225, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(225,225,225, 255);\n"
"    color: rgba(75,75,75,255)\n"
"}")
        self.btn_hits.setAutoRepeatDelay(305)
        self.btn_hits.setObjectName("btn_hits")
        self.verticalLayout_9.addWidget(self.btn_hits)
        self.btn_spectrum = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_spectrum.sizePolicy().hasHeightForWidth())
        self.btn_spectrum.setSizePolicy(sizePolicy)
        self.btn_spectrum.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_spectrum.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_spectrum.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_spectrum.setFont(font)
        self.btn_spectrum.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(225,225,225, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(225,225,225, 255);\n"
"    color: rgba(75,75,75,255)\n"
"}")
        self.btn_spectrum.setAutoRepeatDelay(305)
        self.btn_spectrum.setObjectName("btn_spectrum")
        self.verticalLayout_9.addWidget(self.btn_spectrum)
        self.btn_related = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_related.sizePolicy().hasHeightForWidth())
        self.btn_related.setSizePolicy(sizePolicy)
        self.btn_related.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_related.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_related.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_related.setFont(font)
        self.btn_related.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(225,225,225, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(225,225,225, 255);\n"
"    color: rgba(75,75,75,255)\n"
"}")
        self.btn_related.setAutoRepeatDelay(305)
        self.btn_related.setObjectName("btn_related")
        self.verticalLayout_9.addWidget(self.btn_related)
        self.frame_sidebarspacer_2 = QtWidgets.QFrame(self.frame_sidebar_plot)
        self.frame_sidebarspacer_2.setMinimumSize(QtCore.QSize(121, 0))
        self.frame_sidebarspacer_2.setMaximumSize(QtCore.QSize(121, 16777215))
        self.frame_sidebarspacer_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_sidebarspacer_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sidebarspacer_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sidebarspacer_2.setObjectName("frame_sidebarspacer_2")
        self.verticalLayout_9.addWidget(self.frame_sidebarspacer_2)
        self.btn_masst = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_masst.sizePolicy().hasHeightForWidth())
        self.btn_masst.setSizePolicy(sizePolicy)
        self.btn_masst.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_masst.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_masst.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_masst.setFont(font)
        self.btn_masst.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(225,225,225, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(225,225,225, 255);\n"
"    color: rgba(75,75,75,255)\n"
"}")
        self.btn_masst.setAutoRepeatDelay(305)
        self.btn_masst.setObjectName("btn_masst")
        self.verticalLayout_9.addWidget(self.btn_masst)
        self.horizontalLayout_2.addWidget(self.frame_sidebar_plot)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_plotparams = QtWidgets.QFrame(self.page)
        self.frame_plotparams.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0  rgba(200,200,200,255), stop:1  rgba(240,240,240,255));")
        self.frame_plotparams.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plotparams.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plotparams.setObjectName("frame_plotparams")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_plotparams)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_plotparams)
        self.frame_5.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_5.setMaximumSize(QtCore.QSize(700, 700))
        self.frame_5.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(400, 400))
        self.label.setMaximumSize(QtCore.QSize(400, 400))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_plotparams)
        self.treeWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.treeWidget.setStyleSheet("QTreeView {\n"
"    border-top: 2px solid rgb(70,70,70);\n"
"    border-bottom: 1px solid rgb(70,70,70);\n"
"    border-left: 1px solid rgb(70,70,70);\n"
"    border-right: 1px solid rgb(70,70,70);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(70,70,70,50);\n"
"    padding: 2px;\n"
"    font-size: 9pt;\n"
"    border-style: none;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #rgb(70,70,70);\n"
"}\n"
"QWidget {\n"
"    background-color: rgba(70,70,70,25);\n"
"    color: rgb(70,70,70);\n"
"}\n"
"\n"
"QTreeView {\n"
"    gridline-color: rgb(70,70,70);\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"            border: 1px solid #555555;\n"
"            border-radius: 2px;\n"
"            background: rgb(70,70,70);\n"
"            height:20px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"            background: none;\n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            border-radius: 2px;\n"
"            background-color: rgb(50,50,50);\n"
"        }\n"
"        QScrollBar::add-line:horizontal {       \n"
"            width: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:horizontal {\n"
"            width: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"            border: 1px solid #555555;\n"
"            border-radius: 2px;\n"
"            background: rgb(70,70,70);\n"
"            height:20px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            border-radius: 2px;\n"
"            background-color: rgb(50,50,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            width: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            width: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"\n"
"QTreeView::hideColumn(3)\n"
"")
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.verticalLayout_2.addWidget(self.frame_plotparams)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_specpage = QtWidgets.QFrame(self.page_2)
        self.frame_specpage.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0  rgba(200,200,200,255), stop:1  rgba(240,240,240,255));")
        self.frame_specpage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_specpage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_specpage.setObjectName("frame_specpage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_specpage)
        self.verticalLayout_5.setContentsMargins(13, 13, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_spec = QtWidgets.QFrame(self.frame_specpage)
        self.frame_spec.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_spec.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_spec.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_spec.setObjectName("frame_spec")
        self.verticalLayout_5.addWidget(self.frame_spec)
        self.verticalLayout_3.addWidget(self.frame_specpage)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.page_3)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0  rgba(200,200,200,255), stop:1  rgba(240,240,240,255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_abundance = QtWidgets.QFrame(self.frame)
        self.frame_abundance.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_abundance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_abundance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_abundance.setObjectName("frame_abundance")
        self.verticalLayout_7.addWidget(self.frame_abundance)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.page_4)
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0  rgba(200,200,200,255), stop:1  rgba(240,240,240,255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_4)
        self.credits_bar = QtWidgets.QFrame(self.centralwidget)
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_bar.setStyleSheet("background-color: rgb(40,40,40);")
        self.credits_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_label_credits = QtWidgets.QFrame(self.credits_bar)
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_27.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_credits = QtWidgets.QLabel(self.frame_label_credits)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(150,150,150);")
        self.label_credits.setText("")
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_27.addWidget(self.label_credits)
        self.horizontalLayout_15.addWidget(self.frame_label_credits)
        self.frame_grip_corner = QtWidgets.QFrame(self.credits_bar)
        self.frame_grip_corner.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip_corner.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip_corner.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.frame_grip_corner.setStyleSheet("")
        self.frame_grip_corner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip_corner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip_corner.setObjectName("frame_grip_corner")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_grip_corner)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_15.addWidget(self.frame_grip_corner)
        self.verticalLayout.addWidget(self.credits_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Compound Details</span></p></body></html>"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.btn_abund.setToolTip(_translate("MainWindow", "Data Review Raw Feature Plot"))
        self.btn_abund.setText(_translate("MainWindow", "Abundance"))
        self.btn_hits.setToolTip(_translate("MainWindow", "m/z vs RT Feature Plot by Group Set"))
        self.btn_hits.setText(_translate("MainWindow", "Hits"))
        self.btn_spectrum.setToolTip(_translate("MainWindow", "Principal Component Analysis"))
        self.btn_spectrum.setText(_translate("MainWindow", "Spectrum"))
        self.btn_related.setToolTip(_translate("MainWindow", "Kendrick Mass Defect vs Nominal Mass"))
        self.btn_related.setText(_translate("MainWindow", "Related"))
        self.btn_masst.setToolTip(_translate("MainWindow", "Kendrick Mass Defect vs Nominal Mass"))
        self.btn_masst.setText(_translate("MainWindow", "MASST Search"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Compound"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Formula"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Neutral mass"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "PPM error"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "orgin"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "smiles"))


import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
