# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 770)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 770))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgba(0,0,0,0)")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
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
        self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"background-image: url(:/resources/icons/24x24/icontranscolorless.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.horizontalLayout_13.addWidget(self.frame_icon_top_bar)
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
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons/16x16/cil-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setFlat(False)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_14.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy)
        self.btn_maximize.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_maximize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_maximize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/icons/16x16/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximize.setIcon(icon1)
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_14.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/icons/16x16/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_14.addWidget(self.btn_close)
        self.horizontalLayout_12.addWidget(self.frame_btns_right)
        self._3.addWidget(self.frame_top_btns)
        self.horizontalLayout_3.addWidget(self.frame_title)
        self.verticalLayout.addWidget(self.title_bar)
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(34, 34, 34, 255), stop:1 rgba(52, 52, 52, 255));")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.drop_shadow_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_sidebar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_sidebar.setMaximumSize(QtCore.QSize(75, 16777215))
        self.frame_sidebar.setStyleSheet("")
        self.frame_sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sidebar.setObjectName("frame_sidebar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_sidebar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_import = QtWidgets.QPushButton(self.frame_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import.sizePolicy().hasHeightForWidth())
        self.btn_import.setSizePolicy(sizePolicy)
        self.btn_import.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_import.setMaximumSize(QtCore.QSize(16777215, 75))
        self.btn_import.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgb(35, 35, 35)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: transparent\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_import.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/icons/24x24/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_import.setIcon(icon3)
        self.btn_import.setAutoRepeatDelay(305)
        self.btn_import.setObjectName("btn_import")
        self.verticalLayout_2.addWidget(self.btn_import)
        self.btn_filter = QtWidgets.QPushButton(self.frame_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_filter.sizePolicy().hasHeightForWidth())
        self.btn_filter.setSizePolicy(sizePolicy)
        self.btn_filter.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_filter.setMaximumSize(QtCore.QSize(16777215, 75))
        self.btn_filter.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgb(35, 35, 35)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: transparent\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_filter.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/icons/24x24/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filter.setIcon(icon4)
        self.btn_filter.setAutoRepeatDelay(305)
        self.btn_filter.setObjectName("btn_filter")
        self.verticalLayout_2.addWidget(self.btn_filter)
        self.btn_parameters = QtWidgets.QPushButton(self.frame_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_parameters.sizePolicy().hasHeightForWidth())
        self.btn_parameters.setSizePolicy(sizePolicy)
        self.btn_parameters.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_parameters.setMaximumSize(QtCore.QSize(16777215, 75))
        self.btn_parameters.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgb(35, 35, 35)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: transparent\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_parameters.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resources/icons/24x24/cil-equalizer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_parameters.setIcon(icon5)
        self.btn_parameters.setAutoRepeatDelay(305)
        self.btn_parameters.setObjectName("btn_parameters")
        self.verticalLayout_2.addWidget(self.btn_parameters)
        self.btn_plots = QtWidgets.QPushButton(self.frame_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plots.sizePolicy().hasHeightForWidth())
        self.btn_plots.setSizePolicy(sizePolicy)
        self.btn_plots.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_plots.setMaximumSize(QtCore.QSize(16777215, 75))
        self.btn_plots.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgb(35, 35, 35)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: transparent\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_plots.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/resources/icons/24x24/cil-chart-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_plots.setIcon(icon6)
        self.btn_plots.setAutoRepeatDelay(305)
        self.btn_plots.setObjectName("btn_plots")
        self.verticalLayout_2.addWidget(self.btn_plots)
        self.btn_search = QtWidgets.QPushButton(self.frame_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_search.setMaximumSize(QtCore.QSize(16777215, 75))
        self.btn_search.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgb(35, 35, 35)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: transparent\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_search.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/resources/icons/24x24/cil-zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search.setIcon(icon7)
        self.btn_search.setAutoRepeatDelay(305)
        self.btn_search.setObjectName("btn_search")
        self.verticalLayout_2.addWidget(self.btn_search)
        self.btn_info = QtWidgets.QPushButton(self.frame_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_info.setMaximumSize(QtCore.QSize(16777215, 75))
        self.btn_info.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgb(35, 35, 35)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: transparent\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_info.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/resources/icons/24x24/cil-description.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_info.setIcon(icon8)
        self.btn_info.setAutoRepeatDelay(305)
        self.btn_info.setObjectName("btn_info")
        self.verticalLayout_2.addWidget(self.btn_info)
        self.frame_sidebarspacer = QtWidgets.QFrame(self.frame_sidebar)
        self.frame_sidebarspacer.setStyleSheet("background-color: rgb(35,35,35)")
        self.frame_sidebarspacer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sidebarspacer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sidebarspacer.setObjectName("frame_sidebarspacer")
        self.verticalLayout_2.addWidget(self.frame_sidebarspacer)
        self.btn_run = QtWidgets.QPushButton(self.frame_sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_run.sizePolicy().hasHeightForWidth())
        self.btn_run.setSizePolicy(sizePolicy)
        self.btn_run.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_run.setMaximumSize(QtCore.QSize(16777215, 75))
        self.btn_run.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_run.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/resources/icons/24x24/cil-media-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_run.setIcon(icon9)
        self.btn_run.setAutoRepeatDelay(305)
        self.btn_run.setObjectName("btn_run")
        self.verticalLayout_2.addWidget(self.btn_run)
        self.horizontalLayout.addWidget(self.frame_sidebar)
        self.content_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content_bar.setStyleSheet("background-color: none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.content_bar)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_bar)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")
        self.import_page = QtWidgets.QWidget()
        self.import_page.setObjectName("import_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.import_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_import = QtWidgets.QFrame(self.import_page)
        self.frame_import.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_import.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_import.setObjectName("frame_import")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_import)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lbl_splmdt_2 = QtWidgets.QLabel(self.frame_import)
        self.lbl_splmdt_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_splmdt_2.setFont(font)
        self.lbl_splmdt_2.setStyleSheet("color : rgb(212, 212, 212)")
        self.lbl_splmdt_2.setObjectName("lbl_splmdt_2")
        self.verticalLayout_8.addWidget(self.lbl_splmdt_2)
        self.frame_11 = QtWidgets.QFrame(self.frame_import)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_load_session = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load_session.sizePolicy().hasHeightForWidth())
        self.btn_load_session.setSizePolicy(sizePolicy)
        self.btn_load_session.setMinimumSize(QtCore.QSize(325, 50))
        self.btn_load_session.setMaximumSize(QtCore.QSize(325, 50))
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
        self.btn_load_session.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load_session.setFont(font)
        self.btn_load_session.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_load_session.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 62, 62)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/resources/icons/16x16/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_load_session.setIcon(icon10)
        self.btn_load_session.setAutoRepeatDelay(305)
        self.btn_load_session.setObjectName("btn_load_session")
        self.horizontalLayout_7.addWidget(self.btn_load_session)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.frame_import2 = QtWidgets.QFrame(self.frame_import)
        self.frame_import2.setMaximumSize(QtCore.QSize(16777215, 325))
        self.frame_import2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_import2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_import2.setObjectName("frame_import2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_import2)
        self.horizontalLayout_5.setContentsMargins(40, 0, 0, 10)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_importbtns = QtWidgets.QFrame(self.frame_import2)
        self.frame_importbtns.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_importbtns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_importbtns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_importbtns.setObjectName("frame_importbtns")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_importbtns)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_import_pktbl = QtWidgets.QPushButton(self.frame_importbtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import_pktbl.sizePolicy().hasHeightForWidth())
        self.btn_import_pktbl.setSizePolicy(sizePolicy)
        self.btn_import_pktbl.setMinimumSize(QtCore.QSize(225, 50))
        self.btn_import_pktbl.setMaximumSize(QtCore.QSize(200, 50))
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
        self.btn_import_pktbl.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_import_pktbl.setFont(font)
        self.btn_import_pktbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_import_pktbl.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 62, 62)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_import_pktbl.setIcon(icon10)
        self.btn_import_pktbl.setAutoRepeatDelay(305)
        self.btn_import_pktbl.setObjectName("btn_import_pktbl")
        self.verticalLayout_6.addWidget(self.btn_import_pktbl)
        self.btn_import_spllist = QtWidgets.QPushButton(self.frame_importbtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import_spllist.sizePolicy().hasHeightForWidth())
        self.btn_import_spllist.setSizePolicy(sizePolicy)
        self.btn_import_spllist.setMinimumSize(QtCore.QSize(225, 50))
        self.btn_import_spllist.setMaximumSize(QtCore.QSize(200, 50))
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
        self.btn_import_spllist.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_import_spllist.setFont(font)
        self.btn_import_spllist.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_import_spllist.setIcon(icon10)
        self.btn_import_spllist.setAutoRepeatDelay(305)
        self.btn_import_spllist.setObjectName("btn_import_spllist")
        self.verticalLayout_6.addWidget(self.btn_import_spllist)
        self.btn_import_splmdt = QtWidgets.QPushButton(self.frame_importbtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import_splmdt.sizePolicy().hasHeightForWidth())
        self.btn_import_splmdt.setSizePolicy(sizePolicy)
        self.btn_import_splmdt.setMinimumSize(QtCore.QSize(225, 50))
        self.btn_import_splmdt.setMaximumSize(QtCore.QSize(200, 50))
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
        self.btn_import_splmdt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_import_splmdt.setFont(font)
        self.btn_import_splmdt.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 57, 57)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_import_splmdt.setIcon(icon10)
        self.btn_import_splmdt.setAutoRepeatDelay(305)
        self.btn_import_splmdt.setObjectName("btn_import_splmdt")
        self.verticalLayout_6.addWidget(self.btn_import_splmdt)
        self.btn_import_msp = QtWidgets.QPushButton(self.frame_importbtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import_msp.sizePolicy().hasHeightForWidth())
        self.btn_import_msp.setSizePolicy(sizePolicy)
        self.btn_import_msp.setMinimumSize(QtCore.QSize(225, 50))
        self.btn_import_msp.setMaximumSize(QtCore.QSize(200, 50))
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
        self.btn_import_msp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_import_msp.setFont(font)
        self.btn_import_msp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_import_msp.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 62, 62)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_import_msp.setIcon(icon10)
        self.btn_import_msp.setAutoRepeatDelay(305)
        self.btn_import_msp.setObjectName("btn_import_msp")
        self.verticalLayout_6.addWidget(self.btn_import_msp)
        self.btn_import_outdir = QtWidgets.QPushButton(self.frame_importbtns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import_outdir.sizePolicy().hasHeightForWidth())
        self.btn_import_outdir.setSizePolicy(sizePolicy)
        self.btn_import_outdir.setMinimumSize(QtCore.QSize(225, 50))
        self.btn_import_outdir.setMaximumSize(QtCore.QSize(200, 50))
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
        self.btn_import_outdir.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_import_outdir.setFont(font)
        self.btn_import_outdir.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(55, 55, 55)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_import_outdir.setIcon(icon10)
        self.btn_import_outdir.setAutoRepeatDelay(305)
        self.btn_import_outdir.setObjectName("btn_import_outdir")
        self.verticalLayout_6.addWidget(self.btn_import_outdir)
        self.horizontalLayout_5.addWidget(self.frame_importbtns)
        self.frame_importfiles = QtWidgets.QFrame(self.frame_import2)
        self.frame_importfiles.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_importfiles.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_importfiles.setObjectName("frame_importfiles")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_importfiles)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbl_pktbl = QtWidgets.QLabel(self.frame_importfiles)
        self.lbl_pktbl.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_pktbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pktbl.setFont(font)
        self.lbl_pktbl.setStyleSheet("color : rgb(212, 212, 212)")
        self.lbl_pktbl.setObjectName("lbl_pktbl")
        self.verticalLayout_7.addWidget(self.lbl_pktbl)
        self.lbl_spllist = QtWidgets.QLabel(self.frame_importfiles)
        self.lbl_spllist.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_spllist.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_spllist.setFont(font)
        self.lbl_spllist.setStyleSheet("color : rgb(212, 212, 212)")
        self.lbl_spllist.setObjectName("lbl_spllist")
        self.verticalLayout_7.addWidget(self.lbl_spllist)
        self.lbl_splmdt = QtWidgets.QLabel(self.frame_importfiles)
        self.lbl_splmdt.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_splmdt.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_splmdt.setFont(font)
        self.lbl_splmdt.setStyleSheet("color : rgb(212, 212, 212)")
        self.lbl_splmdt.setObjectName("lbl_splmdt")
        self.verticalLayout_7.addWidget(self.lbl_splmdt)
        self.lbl_msp = QtWidgets.QLabel(self.frame_importfiles)
        self.lbl_msp.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_msp.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_msp.setFont(font)
        self.lbl_msp.setStyleSheet("color : rgb(212, 212, 212)")
        self.lbl_msp.setObjectName("lbl_msp")
        self.verticalLayout_7.addWidget(self.lbl_msp)
        self.lbl_outdir = QtWidgets.QLabel(self.frame_importfiles)
        self.lbl_outdir.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_outdir.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_outdir.setFont(font)
        self.lbl_outdir.setStyleSheet("color : rgb(212, 212, 212)")
        self.lbl_outdir.setObjectName("lbl_outdir")
        self.verticalLayout_7.addWidget(self.lbl_outdir)
        self.horizontalLayout_5.addWidget(self.frame_importfiles)
        self.verticalLayout_8.addWidget(self.frame_import2)
        self.frame_mispicked = QtWidgets.QFrame(self.frame_import)
        self.frame_mispicked.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_mispicked.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_mispicked.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_mispicked.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mispicked.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mispicked.setObjectName("frame_mispicked")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_mispicked)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem1)
        self.verticalLayout_8.addWidget(self.frame_mispicked)
        self.verticalLayout_5.addWidget(self.frame_import)
        self.stackedWidget.addWidget(self.import_page)
        self.filter_page = QtWidgets.QWidget()
        self.filter_page.setObjectName("filter_page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.filter_page)
        self.verticalLayout_9.setContentsMargins(30, 25, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_filter = QtWidgets.QFrame(self.filter_page)
        self.frame_filter.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_filter.setObjectName("frame_filter")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_filter)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_mp_params = QtWidgets.QFrame(self.frame_filter)
        self.frame_mp_params.setMinimumSize(QtCore.QSize(450, 300))
        self.frame_mp_params.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_mp_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mp_params.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mp_params.setObjectName("frame_mp_params")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_mp_params)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.checkBox_mp = QtWidgets.QCheckBox(self.frame_mp_params)
        self.checkBox_mp.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_mp.setMaximumSize(QtCore.QSize(16777215, 35))
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
        self.checkBox_mp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_mp.setFont(font)
        self.checkBox_mp.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_mp.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_mp.setCheckable(True)
        self.checkBox_mp.setChecked(True)
        self.checkBox_mp.setObjectName("checkBox_mp")
        self.verticalLayout_12.addWidget(self.checkBox_mp)
        self.frame_mp_params3 = QtWidgets.QFrame(self.frame_mp_params)
        self.frame_mp_params3.setMinimumSize(QtCore.QSize(0, 190))
        self.frame_mp_params3.setMaximumSize(QtCore.QSize(16777215, 240))
        self.frame_mp_params3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mp_params3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mp_params3.setObjectName("frame_mp_params3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_mp_params3)
        self.gridLayout.setContentsMargins(30, 0, 10, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_merge = QtWidgets.QCheckBox(self.frame_mp_params3)
        self.checkBox_merge.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_merge.setMaximumSize(QtCore.QSize(16777215, 35))
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
        self.checkBox_merge.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_merge.setFont(font)
        self.checkBox_merge.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"\n"
"")
        self.checkBox_merge.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_merge.setCheckable(True)
        self.checkBox_merge.setChecked(True)
        self.checkBox_merge.setObjectName("checkBox_merge")
        self.gridLayout.addWidget(self.checkBox_merge, 0, 0, 1, 1)
        self.lineEdit_ringwin = QtWidgets.QLineEdit(self.frame_mp_params3)
        self.lineEdit_ringwin.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_ringwin.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.lineEdit_ringwin.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_ringwin.setFont(font)
        self.lineEdit_ringwin.setStyleSheet("QLineEdit{ \n"
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
        self.lineEdit_ringwin.setObjectName("lineEdit_ringwin")
        self.gridLayout.addWidget(self.lineEdit_ringwin, 1, 1, 1, 1)
        self.combo_maxisoshift = QtWidgets.QComboBox(self.frame_mp_params3)
        self.combo_maxisoshift.setMinimumSize(QtCore.QSize(0, 30))
        self.combo_maxisoshift.setMaximumSize(QtCore.QSize(150, 16777215))
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
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.combo_maxisoshift.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.combo_maxisoshift.setFont(font)
        self.combo_maxisoshift.setStyleSheet("QComboBox{ \n"
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
        self.combo_maxisoshift.setObjectName("combo_maxisoshift")
        self.combo_maxisoshift.addItem("")
        self.combo_maxisoshift.addItem("")
        self.combo_maxisoshift.addItem("")
        self.combo_maxisoshift.addItem("")
        self.combo_maxisoshift.addItem("")
        self.combo_maxisoshift.addItem("")
        self.gridLayout.addWidget(self.combo_maxisoshift, 4, 1, 1, 1)
        self.lbl_ringwin = QtWidgets.QLabel(self.frame_mp_params3)
        self.lbl_ringwin.setMinimumSize(QtCore.QSize(175, 0))
        self.lbl_ringwin.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ringwin.setFont(font)
        self.lbl_ringwin.setObjectName("lbl_ringwin")
        self.gridLayout.addWidget(self.lbl_ringwin, 1, 0, 1, 1)
        self.lineEdit_isowin = QtWidgets.QLineEdit(self.frame_mp_params3)
        self.lineEdit_isowin.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_isowin.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.lineEdit_isowin.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_isowin.setFont(font)
        self.lineEdit_isowin.setStyleSheet("QLineEdit{ \n"
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
        self.lineEdit_isowin.setObjectName("lineEdit_isowin")
        self.gridLayout.addWidget(self.lineEdit_isowin, 2, 1, 1, 1)
        self.lbl_isowin = QtWidgets.QLabel(self.frame_mp_params3)
        self.lbl_isowin.setMinimumSize(QtCore.QSize(200, 0))
        self.lbl_isowin.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_isowin.setFont(font)
        self.lbl_isowin.setObjectName("lbl_isowin")
        self.gridLayout.addWidget(self.lbl_isowin, 2, 0, 1, 1)
        self.lineEdit_rtwin = QtWidgets.QLineEdit(self.frame_mp_params3)
        self.lineEdit_rtwin.setMinimumSize(QtCore.QSize(6, 30))
        self.lineEdit_rtwin.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.lineEdit_rtwin.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_rtwin.setFont(font)
        self.lineEdit_rtwin.setStyleSheet("QLineEdit{ \n"
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
        self.lineEdit_rtwin.setObjectName("lineEdit_rtwin")
        self.gridLayout.addWidget(self.lineEdit_rtwin, 3, 1, 1, 1)
        self.lbl_maxisoshift = QtWidgets.QLabel(self.frame_mp_params3)
        self.lbl_maxisoshift.setMinimumSize(QtCore.QSize(200, 0))
        self.lbl_maxisoshift.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_maxisoshift.setFont(font)
        self.lbl_maxisoshift.setObjectName("lbl_maxisoshift")
        self.gridLayout.addWidget(self.lbl_maxisoshift, 4, 0, 1, 1)
        self.lbl_rtwin = QtWidgets.QLabel(self.frame_mp_params3)
        self.lbl_rtwin.setMinimumSize(QtCore.QSize(200, 0))
        self.lbl_rtwin.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rtwin.setFont(font)
        self.lbl_rtwin.setObjectName("lbl_rtwin")
        self.gridLayout.addWidget(self.lbl_rtwin, 3, 0, 1, 1)
        self.verticalLayout_12.addWidget(self.frame_mp_params3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.checkBox_blankfilter = QtWidgets.QCheckBox(self.frame_mp_params)
        self.checkBox_blankfilter.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_blankfilter.setMaximumSize(QtCore.QSize(16777215, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox_blankfilter.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_blankfilter.setFont(font)
        self.checkBox_blankfilter.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_blankfilter.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_blankfilter.setCheckable(True)
        self.checkBox_blankfilter.setChecked(True)
        self.checkBox_blankfilter.setObjectName("checkBox_blankfilter")
        self.verticalLayout_12.addWidget(self.checkBox_blankfilter)
        self.frame_blankfil_params4_3 = QtWidgets.QFrame(self.frame_mp_params)
        self.frame_blankfil_params4_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_blankfil_params4_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_blankfil_params4_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blankfil_params4_3.setObjectName("frame_blankfil_params4_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_blankfil_params4_3)
        self.horizontalLayout_6.setContentsMargins(30, 0, 10, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_blankfil_name_2 = QtWidgets.QLabel(self.frame_blankfil_params4_3)
        self.lbl_blankfil_name_2.setMinimumSize(QtCore.QSize(120, 30))
        self.lbl_blankfil_name_2.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_blankfil_name_2.setFont(font)
        self.lbl_blankfil_name_2.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_blankfil_name_2.setObjectName("lbl_blankfil_name_2")
        self.horizontalLayout_6.addWidget(self.lbl_blankfil_name_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.combo_blankfil_name = QtWidgets.QComboBox(self.frame_blankfil_params4_3)
        self.combo_blankfil_name.setMinimumSize(QtCore.QSize(150, 30))
        self.combo_blankfil_name.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.combo_blankfil_name.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.combo_blankfil_name.setFont(font)
        self.combo_blankfil_name.setStyleSheet("QComboBox{ \n"
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
        self.combo_blankfil_name.setEditable(True)
        self.combo_blankfil_name.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combo_blankfil_name.setObjectName("combo_blankfil_name")
        self.horizontalLayout_6.addWidget(self.combo_blankfil_name)
        self.verticalLayout_12.addWidget(self.frame_blankfil_params4_3)
        spacerItem4 = QtWidgets.QSpacerItem(425, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem4)
        self.checkBox_cv = QtWidgets.QCheckBox(self.frame_mp_params)
        self.checkBox_cv.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_cv.setMaximumSize(QtCore.QSize(16777215, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox_cv.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_cv.setFont(font)
        self.checkBox_cv.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_cv.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_cv.setCheckable(True)
        self.checkBox_cv.setChecked(True)
        self.checkBox_cv.setObjectName("checkBox_cv")
        self.verticalLayout_12.addWidget(self.checkBox_cv)
        self.frame_cv_params3 = QtWidgets.QFrame(self.frame_mp_params)
        self.frame_cv_params3.setMinimumSize(QtCore.QSize(0, 95))
        self.frame_cv_params3.setMaximumSize(QtCore.QSize(16777215, 95))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_cv_params3.setFont(font)
        self.frame_cv_params3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cv_params3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cv_params3.setObjectName("frame_cv_params3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_cv_params3)
        self.gridLayout_2.setContentsMargins(30, 0, 0, 10)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_meancv = QtWidgets.QRadioButton(self.frame_cv_params3)
        self.radioButton_meancv.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_meancv.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.radioButton_meancv.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_meancv.setFont(font)
        self.radioButton_meancv.setStyleSheet("QRadioButton {\n"
"    color:                  #d0d0d0;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"    color:                  rgb(40, 40, 40);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       rgb(212, 212, 212);\n"
"    border:                 4px solid lightgrey;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(40, 40, 40);\n"
"    border:                 4px  solid lightgrey;\n"
"}\n"
"\n"
"")
        self.radioButton_meancv.setChecked(False)
        self.radioButton_meancv.setObjectName("radioButton_meancv")
        self.gridLayout_2.addWidget(self.radioButton_meancv, 4, 0, 1, 1)
        self.lbl_cvthresh = QtWidgets.QLabel(self.frame_cv_params3)
        self.lbl_cvthresh.setMinimumSize(QtCore.QSize(200, 0))
        self.lbl_cvthresh.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cvthresh.setFont(font)
        self.lbl_cvthresh.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_cvthresh.setObjectName("lbl_cvthresh")
        self.gridLayout_2.addWidget(self.lbl_cvthresh, 3, 0, 1, 1)
        self.lineEdit_cvthresh = QtWidgets.QLineEdit(self.frame_cv_params3)
        self.lineEdit_cvthresh.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_cvthresh.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.lineEdit_cvthresh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_cvthresh.setFont(font)
        self.lineEdit_cvthresh.setStyleSheet("QLineEdit{ \n"
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
        self.lineEdit_cvthresh.setObjectName("lineEdit_cvthresh")
        self.gridLayout_2.addWidget(self.lineEdit_cvthresh, 3, 1, 1, 1)
        self.radioButton_medcv = QtWidgets.QRadioButton(self.frame_cv_params3)
        self.radioButton_medcv.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_medcv.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.radioButton_medcv.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_medcv.setFont(font)
        self.radioButton_medcv.setStyleSheet("QRadioButton {\n"
"    color:                  #d0d0d0;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"    color:                  rgb(40, 40, 40);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       rgb(212, 212, 212);\n"
"    border:                 4px solid lightgrey;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(40, 40, 40);\n"
"    border:                 4px  solid lightgrey;\n"
"}\n"
"\n"
"")
        self.radioButton_medcv.setChecked(True)
        self.radioButton_medcv.setObjectName("radioButton_medcv")
        self.gridLayout_2.addWidget(self.radioButton_medcv, 5, 0, 1, 1)
        self.verticalLayout_12.addWidget(self.frame_cv_params3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.checkBox_decon = QtWidgets.QCheckBox(self.frame_mp_params)
        self.checkBox_decon.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_decon.setMaximumSize(QtCore.QSize(16777215, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox_decon.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_decon.setFont(font)
        self.checkBox_decon.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_decon.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_decon.setCheckable(True)
        self.checkBox_decon.setChecked(True)
        self.checkBox_decon.setObjectName("checkBox_decon")
        self.verticalLayout_12.addWidget(self.checkBox_decon)
        self.frame_insource_params = QtWidgets.QFrame(self.frame_mp_params)
        self.frame_insource_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_insource_params.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_insource_params.setObjectName("frame_insource_params")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_insource_params)
        self.gridLayout_8.setContentsMargins(30, 0, 10, 0)
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lbl_insourcethresh = QtWidgets.QLabel(self.frame_insource_params)
        self.lbl_insourcethresh.setMinimumSize(QtCore.QSize(119, 30))
        self.lbl_insourcethresh.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_insourcethresh.setFont(font)
        self.lbl_insourcethresh.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_insourcethresh.setObjectName("lbl_insourcethresh")
        self.gridLayout_8.addWidget(self.lbl_insourcethresh, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 2, 1, 1)
        self.lineEdit_insourcethresh = QtWidgets.QLineEdit(self.frame_insource_params)
        self.lineEdit_insourcethresh.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_insourcethresh.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.lineEdit_insourcethresh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_insourcethresh.setFont(font)
        self.lineEdit_insourcethresh.setStyleSheet("QLineEdit{ \n"
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
        self.lineEdit_insourcethresh.setObjectName("lineEdit_insourcethresh")
        self.gridLayout_8.addWidget(self.lineEdit_insourcethresh, 0, 3, 1, 1)
        self.verticalLayout_12.addWidget(self.frame_insource_params)
        self.verticalLayout_10.addWidget(self.frame_mp_params)
        self.verticalLayout_9.addWidget(self.frame_filter)
        self.stackedWidget.addWidget(self.filter_page)
        self.param_page = QtWidgets.QWidget()
        self.param_page.setObjectName("param_page")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.param_page)
        self.verticalLayout_20.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_param = QtWidgets.QFrame(self.param_page)
        self.frame_param.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_param.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_param.setObjectName("frame_param")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_param)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_blankfil_params = QtWidgets.QFrame(self.frame_param)
        self.frame_blankfil_params.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_blankfil_params.setMaximumSize(QtCore.QSize(430, 500))
        self.frame_blankfil_params.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_blankfil_params.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blankfil_params.setObjectName("frame_blankfil_params")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_blankfil_params)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.lbl_grpprs_2 = QtWidgets.QLabel(self.frame_blankfil_params)
        self.lbl_grpprs_2.setMinimumSize(QtCore.QSize(200, 50))
        self.lbl_grpprs_2.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_grpprs_2.setFont(font)
        self.lbl_grpprs_2.setStyleSheet("color : rgb(212, 212, 212)")
        self.lbl_grpprs_2.setObjectName("lbl_grpprs_2")
        self.verticalLayout_29.addWidget(self.lbl_grpprs_2)
        self.frame_blankfil_params2_2 = QtWidgets.QFrame(self.frame_blankfil_params)
        self.frame_blankfil_params2_2.setMinimumSize(QtCore.QSize(275, 75))
        self.frame_blankfil_params2_2.setMaximumSize(QtCore.QSize(275, 75))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_blankfil_params2_2.setFont(font)
        self.frame_blankfil_params2_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_blankfil_params2_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blankfil_params2_2.setObjectName("frame_blankfil_params2_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_blankfil_params2_2)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.radioButton_blankfilter_abs = QtWidgets.QRadioButton(self.frame_blankfil_params2_2)
        self.radioButton_blankfilter_abs.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButton_blankfilter_abs.setMaximumSize(QtCore.QSize(200, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.radioButton_blankfilter_abs.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_blankfilter_abs.setFont(font)
        self.radioButton_blankfilter_abs.setStyleSheet("QRadioButton {\n"
"    color:                  #d0d0d0;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"    color:                  rgb(40, 40, 40);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       rgb(212, 212, 212);\n"
"    border:                 4px solid lightgrey;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(40, 40, 40);\n"
"    border:                 4px  solid lightgrey;\n"
"}\n"
"\n"
"")
        self.radioButton_blankfilter_abs.setChecked(False)
        self.radioButton_blankfilter_abs.setObjectName("radioButton_blankfilter_abs")
        self.gridLayout_9.addWidget(self.radioButton_blankfilter_abs, 1, 0, 1, 1)
        self.lineEdit_blankfilter_relthresh = QtWidgets.QLineEdit(self.frame_blankfil_params2_2)
        self.lineEdit_blankfilter_relthresh.setMinimumSize(QtCore.QSize(6, 30))
        self.lineEdit_blankfilter_relthresh.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.lineEdit_blankfilter_relthresh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_blankfilter_relthresh.setFont(font)
        self.lineEdit_blankfilter_relthresh.setStyleSheet("QLineEdit{ \n"
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
        self.lineEdit_blankfilter_relthresh.setObjectName("lineEdit_blankfilter_relthresh")
        self.gridLayout_9.addWidget(self.lineEdit_blankfilter_relthresh, 3, 1, 1, 1)
        self.lineEdit_blankfilter_absthresh = QtWidgets.QLineEdit(self.frame_blankfil_params2_2)
        self.lineEdit_blankfilter_absthresh.setMinimumSize(QtCore.QSize(6, 30))
        self.lineEdit_blankfilter_absthresh.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.lineEdit_blankfilter_absthresh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_blankfilter_absthresh.setFont(font)
        self.lineEdit_blankfilter_absthresh.setStyleSheet("QLineEdit{ \n"
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
        self.lineEdit_blankfilter_absthresh.setObjectName("lineEdit_blankfilter_absthresh")
        self.gridLayout_9.addWidget(self.lineEdit_blankfilter_absthresh, 1, 1, 1, 1)
        self.radioButton_blankfilter_rel = QtWidgets.QRadioButton(self.frame_blankfil_params2_2)
        self.radioButton_blankfilter_rel.setMinimumSize(QtCore.QSize(200, 30))
        self.radioButton_blankfilter_rel.setMaximumSize(QtCore.QSize(30, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 208, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.radioButton_blankfilter_rel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_blankfilter_rel.setFont(font)
        self.radioButton_blankfilter_rel.setStyleSheet("QRadioButton {\n"
"    color:                  #d0d0d0;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"    color:                  rgb(40, 40, 40);\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       rgb(212, 212, 212);\n"
"    border:                 4px solid lightgrey;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(40, 40, 40);\n"
"    border:                 4px  solid lightgrey;\n"
"}\n"
"\n"
"")
        self.radioButton_blankfilter_rel.setChecked(True)
        self.radioButton_blankfilter_rel.setObjectName("radioButton_blankfilter_rel")
        self.gridLayout_9.addWidget(self.radioButton_blankfilter_rel, 3, 0, 1, 1)
        self.verticalLayout_29.addWidget(self.frame_blankfil_params2_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem7)
        self.horizontalLayout_8.addWidget(self.frame_blankfil_params)
        self.frame_calc = QtWidgets.QFrame(self.frame_param)
        self.frame_calc.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame_calc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_calc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calc.setObjectName("frame_calc")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_calc)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.lbl_calc = QtWidgets.QLabel(self.frame_calc)
        self.lbl_calc.setMinimumSize(QtCore.QSize(0, 35))
        self.lbl_calc.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_calc.setFont(font)
        self.lbl_calc.setObjectName("lbl_calc")
        self.verticalLayout_21.addWidget(self.lbl_calc)
        self.checkBox_fc = QtWidgets.QCheckBox(self.frame_calc)
        self.checkBox_fc.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_fc.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_fc.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_fc.setFont(font)
        self.checkBox_fc.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }")
        self.checkBox_fc.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_fc.setCheckable(True)
        self.checkBox_fc.setChecked(True)
        self.checkBox_fc.setObjectName("checkBox_fc")
        self.verticalLayout_21.addWidget(self.checkBox_fc)
        self.checkBox_ttest = QtWidgets.QCheckBox(self.frame_calc)
        self.checkBox_ttest.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_ttest.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_ttest.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_ttest.setFont(font)
        self.checkBox_ttest.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }")
        self.checkBox_ttest.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_ttest.setCheckable(True)
        self.checkBox_ttest.setChecked(True)
        self.checkBox_ttest.setObjectName("checkBox_ttest")
        self.verticalLayout_21.addWidget(self.checkBox_ttest)
        self.frame_statstgrps = QtWidgets.QFrame(self.frame_calc)
        self.frame_statstgrps.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_statstgrps.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_statstgrps.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_statstgrps.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_statstgrps.setObjectName("frame_statstgrps")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_statstgrps)
        self.gridLayout_3.setContentsMargins(30, 0, 0, 0)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_expgrp = QtWidgets.QLabel(self.frame_statstgrps)
        self.lbl_expgrp.setMinimumSize(QtCore.QSize(175, 0))
        self.lbl_expgrp.setMaximumSize(QtCore.QSize(175, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lbl_expgrp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_expgrp.setFont(font)
        self.lbl_expgrp.setObjectName("lbl_expgrp")
        self.gridLayout_3.addWidget(self.lbl_expgrp, 0, 0, 1, 1)
        self.checkBox_FDR = QtWidgets.QCheckBox(self.frame_statstgrps)
        self.checkBox_FDR.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_FDR.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_FDR.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_FDR.setFont(font)
        self.checkBox_FDR.setStyleSheet("  QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_FDR.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_FDR.setCheckable(True)
        self.checkBox_FDR.setChecked(True)
        self.checkBox_FDR.setObjectName("checkBox_FDR")
        self.gridLayout_3.addWidget(self.checkBox_FDR, 3, 0, 1, 1)
        self.combo_expgrp = QtWidgets.QComboBox(self.frame_statstgrps)
        self.combo_expgrp.setMinimumSize(QtCore.QSize(125, 30))
        self.combo_expgrp.setMaximumSize(QtCore.QSize(125, 16777215))
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
        self.combo_expgrp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.combo_expgrp.setFont(font)
        self.combo_expgrp.setStyleSheet("QComboBox{ \n"
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
        self.combo_expgrp.setEditable(True)
        self.combo_expgrp.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combo_expgrp.setObjectName("combo_expgrp")
        self.gridLayout_3.addWidget(self.combo_expgrp, 0, 1, 1, 1)
        self.combo_ctrgrp = QtWidgets.QComboBox(self.frame_statstgrps)
        self.combo_ctrgrp.setMinimumSize(QtCore.QSize(125, 30))
        self.combo_ctrgrp.setMaximumSize(QtCore.QSize(125, 16777215))
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
        self.combo_ctrgrp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.combo_ctrgrp.setFont(font)
        self.combo_ctrgrp.setStyleSheet("QComboBox{ \n"
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
        self.combo_ctrgrp.setEditable(True)
        self.combo_ctrgrp.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combo_ctrgrp.setObjectName("combo_ctrgrp")
        self.gridLayout_3.addWidget(self.combo_ctrgrp, 1, 1, 1, 1)
        self.lbl_ctrgrp = QtWidgets.QLabel(self.frame_statstgrps)
        self.lbl_ctrgrp.setMinimumSize(QtCore.QSize(175, 0))
        self.lbl_ctrgrp.setMaximumSize(QtCore.QSize(175, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ctrgrp.setFont(font)
        self.lbl_ctrgrp.setObjectName("lbl_ctrgrp")
        self.gridLayout_3.addWidget(self.lbl_ctrgrp, 1, 0, 1, 1)
        self.verticalLayout_21.addWidget(self.frame_statstgrps)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem8)
        self.horizontalLayout_8.addWidget(self.frame_calc)
        self.frame_plts = QtWidgets.QFrame(self.frame_param)
        self.frame_plts.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_plts.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plts.setObjectName("frame_plts")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_plts)
        self.verticalLayout_22.setContentsMargins(0, 0, -1, 5)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lbl_plotparams = QtWidgets.QLabel(self.frame_plts)
        self.lbl_plotparams.setMinimumSize(QtCore.QSize(0, 35))
        self.lbl_plotparams.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_plotparams.setFont(font)
        self.lbl_plotparams.setObjectName("lbl_plotparams")
        self.verticalLayout_22.addWidget(self.lbl_plotparams)
        self.checkBox_pca = QtWidgets.QCheckBox(self.frame_plts)
        self.checkBox_pca.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_pca.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_pca.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_pca.setFont(font)
        self.checkBox_pca.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_pca.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_pca.setCheckable(True)
        self.checkBox_pca.setChecked(True)
        self.checkBox_pca.setObjectName("checkBox_pca")
        self.verticalLayout_22.addWidget(self.checkBox_pca)
        self.checkBox_dend = QtWidgets.QCheckBox(self.frame_plts)
        self.checkBox_dend.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_dend.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_dend.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_dend.setFont(font)
        self.checkBox_dend.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_dend.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_dend.setCheckable(True)
        self.checkBox_dend.setChecked(True)
        self.checkBox_dend.setObjectName("checkBox_dend")
        self.verticalLayout_22.addWidget(self.checkBox_dend)
        self.checkBox_mzrt = QtWidgets.QCheckBox(self.frame_plts)
        self.checkBox_mzrt.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_mzrt.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_mzrt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_mzrt.setFont(font)
        self.checkBox_mzrt.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_mzrt.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_mzrt.setCheckable(True)
        self.checkBox_mzrt.setChecked(True)
        self.checkBox_mzrt.setObjectName("checkBox_mzrt")
        self.verticalLayout_22.addWidget(self.checkBox_mzrt)
        self.checkBox_kmd = QtWidgets.QCheckBox(self.frame_plts)
        self.checkBox_kmd.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_kmd.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_kmd.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_kmd.setFont(font)
        self.checkBox_kmd.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_kmd.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_kmd.setCheckable(True)
        self.checkBox_kmd.setChecked(True)
        self.checkBox_kmd.setObjectName("checkBox_kmd")
        self.verticalLayout_22.addWidget(self.checkBox_kmd)
        self.checkBox_3dfc = QtWidgets.QCheckBox(self.frame_plts)
        self.checkBox_3dfc.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_3dfc.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_3dfc.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3dfc.setFont(font)
        self.checkBox_3dfc.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_3dfc.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_3dfc.setCheckable(True)
        self.checkBox_3dfc.setChecked(True)
        self.checkBox_3dfc.setObjectName("checkBox_3dfc")
        self.verticalLayout_22.addWidget(self.checkBox_3dfc)
        self.checkBox_volcano = QtWidgets.QCheckBox(self.frame_plts)
        self.checkBox_volcano.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_volcano.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_volcano.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_volcano.setFont(font)
        self.checkBox_volcano.setStyleSheet("  QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }\n"
"")
        self.checkBox_volcano.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_volcano.setCheckable(True)
        self.checkBox_volcano.setChecked(True)
        self.checkBox_volcano.setObjectName("checkBox_volcano")
        self.verticalLayout_22.addWidget(self.checkBox_volcano)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem9)
        self.horizontalLayout_8.addWidget(self.frame_plts)
        self.verticalLayout_20.addWidget(self.frame_param)
        self.frame_pltgroups = QtWidgets.QFrame(self.param_page)
        self.frame_pltgroups.setMinimumSize(QtCore.QSize(0, 350))
        self.frame_pltgroups.setMaximumSize(QtCore.QSize(16777215, 350))
        self.frame_pltgroups.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pltgroups.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pltgroups.setObjectName("frame_pltgroups")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_pltgroups)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.frame_9 = QtWidgets.QFrame(self.frame_pltgroups)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.lbl_pltgroups = QtWidgets.QLabel(self.frame_9)
        self.lbl_pltgroups.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pltgroups.setFont(font)
        self.lbl_pltgroups.setObjectName("lbl_pltgroups")
        self.horizontalLayout_21.addWidget(self.lbl_pltgroups)
        self.verticalLayout_45.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_pltgroups)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_10)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.listWidget_pltgrps = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_pltgrps.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_pltgrps.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_pltgrps.setFont(font)
        self.listWidget_pltgrps.setStyleSheet("QListWidget{\n"
"    border: 0px solid rgb(212,212,212);\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color:rgba(60,60,60,255);\n"
"    color: rgb(212,212,212);\n"
"}\n"
"QListWidget::item:hover\n"
"{\n"
"    background-color:  rgba(255,255,255,15); \n"
"    color: rgb(212,212,212)\n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"    background: rgba(255,255,255,30);\n"
"    color: rgb(212,212,212)\n"
"}\n"
"QScrollBar:vertical {\n"
"            width:15px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"            background-color:rgba(80,80,80,100);\n"
"\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {         \n"
"            min-width: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            background-color: rgba(0,0,0,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.listWidget_pltgrps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_pltgrps.setIconSize(QtCore.QSize(10, 0))
        self.listWidget_pltgrps.setObjectName("listWidget_pltgrps")
        self.verticalLayout_13.addWidget(self.listWidget_pltgrps)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setContentsMargins(5, 10, 5, 0)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_addgroup = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addgroup.sizePolicy().hasHeightForWidth())
        self.btn_addgroup.setSizePolicy(sizePolicy)
        self.btn_addgroup.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_addgroup.setMaximumSize(QtCore.QSize(30, 30))
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
        self.btn_addgroup.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addgroup.setFont(font)
        self.btn_addgroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_addgroup.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 62, 62)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_addgroup.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/resources/icons/20x20/cil-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addgroup.setIcon(icon11)
        self.btn_addgroup.setIconSize(QtCore.QSize(20, 20))
        self.btn_addgroup.setAutoRepeatDelay(305)
        self.btn_addgroup.setObjectName("btn_addgroup")
        self.horizontalLayout_11.addWidget(self.btn_addgroup)
        self.btn_removegroup = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_removegroup.sizePolicy().hasHeightForWidth())
        self.btn_removegroup.setSizePolicy(sizePolicy)
        self.btn_removegroup.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_removegroup.setMaximumSize(QtCore.QSize(30, 30))
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
        self.btn_removegroup.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_removegroup.setFont(font)
        self.btn_removegroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_removegroup.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 62, 62)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_removegroup.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/resources/icons/20x20/cil-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_removegroup.setIcon(icon12)
        self.btn_removegroup.setIconSize(QtCore.QSize(20, 20))
        self.btn_removegroup.setAutoRepeatDelay(305)
        self.btn_removegroup.setObjectName("btn_removegroup")
        self.horizontalLayout_11.addWidget(self.btn_removegroup)
        self.verticalLayout_13.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame_10)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_calc_3 = QtWidgets.QLabel(self.frame_8)
        self.lbl_calc_3.setMinimumSize(QtCore.QSize(0, 25))
        self.lbl_calc_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_calc_3.setFont(font)
        self.lbl_calc_3.setObjectName("lbl_calc_3")
        self.gridLayout_4.addWidget(self.lbl_calc_3, 0, 0, 1, 1)
        self.lbl_calc_2 = QtWidgets.QLabel(self.frame_8)
        self.lbl_calc_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_calc_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_calc_2.setFont(font)
        self.lbl_calc_2.setObjectName("lbl_calc_2")
        self.gridLayout_4.addWidget(self.lbl_calc_2, 0, 1, 1, 1)
        self.lbl_calc_4 = QtWidgets.QLabel(self.frame_8)
        self.lbl_calc_4.setMinimumSize(QtCore.QSize(0, 25))
        self.lbl_calc_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_calc_4.setFont(font)
        self.lbl_calc_4.setObjectName("lbl_calc_4")
        self.gridLayout_4.addWidget(self.lbl_calc_4, 0, 3, 1, 1)
        self.listWidget_orgrps = QtWidgets.QListWidget(self.frame_8)
        self.listWidget_orgrps.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_orgrps.setFont(font)
        self.listWidget_orgrps.setAcceptDrops(True)
        self.listWidget_orgrps.setStyleSheet("QListWidget{\n"
"    border: 0px solid rgb(212,212,212);\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color:rgba(255,255,255,15);\n"
"    color: rgb(212,212,212);\n"
"}\n"
"QListWidget::item:hover\n"
"{\n"
"    background-color:  rgba(255,255,255,15); \n"
"    color: rgb(212,212,212)\n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"    background: rgba(255,255,255,30);\n"
"    color: rgb(212,212,212)\n"
"}\n"
"QScrollBar:vertical {\n"
"            width:15px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {         \n"
"            min-width: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            background-color: rgba(0,0,0,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.listWidget_orgrps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_orgrps.setDragEnabled(True)
        self.listWidget_orgrps.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_orgrps.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_orgrps.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_orgrps.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listWidget_orgrps.setObjectName("listWidget_orgrps")
        self.gridLayout_4.addWidget(self.listWidget_orgrps, 1, 1, 1, 1)
        self.listWidget_allgrps = QtWidgets.QListWidget(self.frame_8)
        self.listWidget_allgrps.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_allgrps.setFont(font)
        self.listWidget_allgrps.setAcceptDrops(True)
        self.listWidget_allgrps.setStyleSheet("QListWidget{\n"
"    border: 0px solid rgb(212,212,212);\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color:rgba(255,255,255,15);\n"
"    color: rgb(212,212,212);\n"
"}\n"
"QListWidget::item:hover\n"
"{\n"
"    background-color:  rgba(255,255,255,15); \n"
"    color: rgb(212,212,212)\n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"    background: rgba(255,255,255,30);\n"
"    color: rgb(212,212,212)\n"
"}\n"
"QScrollBar:vertical {\n"
"            width:15px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {         \n"
"            min-width: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            background-color: rgba(0,0,0,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.listWidget_allgrps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_allgrps.setDragEnabled(True)
        self.listWidget_allgrps.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_allgrps.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_allgrps.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_allgrps.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listWidget_allgrps.setObjectName("listWidget_allgrps")
        self.gridLayout_4.addWidget(self.listWidget_allgrps, 1, 0, 1, 1)
        self.listWidget_andgrps = QtWidgets.QListWidget(self.frame_8)
        self.listWidget_andgrps.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_andgrps.setFont(font)
        self.listWidget_andgrps.setAcceptDrops(True)
        self.listWidget_andgrps.setStyleSheet("QListWidget{\n"
"    border: 0px solid rgb(212,212,212);\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color:rgba(255,255,255,15);\n"
"    color: rgb(212,212,212);\n"
"}\n"
"QListWidget::item:hover\n"
"{\n"
"    background-color:  rgba(255,255,255,15); \n"
"    color: rgb(212,212,212)\n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"    background: rgba(255,255,255,30);\n"
"    color: rgb(212,212,212)\n"
"}\n"
"QScrollBar:vertical {\n"
"            width:15px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {         \n"
"            min-width: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            background-color: rgba(0,0,0,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.listWidget_andgrps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_andgrps.setDragEnabled(True)
        self.listWidget_andgrps.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_andgrps.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_andgrps.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listWidget_andgrps.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listWidget_andgrps.setObjectName("listWidget_andgrps")
        self.gridLayout_4.addWidget(self.listWidget_andgrps, 1, 3, 1, 1)
        self.verticalLayout_16.addWidget(self.frame_8)
        self.frame_coluse = QtWidgets.QFrame(self.frame_2)
        self.frame_coluse.setMinimumSize(QtCore.QSize(100, 30))
        self.frame_coluse.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_coluse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_coluse.setAutoFillBackground(False)
        self.frame_coluse.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_coluse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_coluse.setObjectName("frame_coluse")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_coluse)
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_22.setSpacing(9)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.btn_col1 = QtWidgets.QPushButton(self.frame_coluse)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_col1.sizePolicy().hasHeightForWidth())
        self.btn_col1.setSizePolicy(sizePolicy)
        self.btn_col1.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_col1.setMaximumSize(QtCore.QSize(20, 20))
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
        self.btn_col1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_col1.setFont(font)
        self.btn_col1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_col1.setStyleSheet("QPushButton {    \n"
"    border: 2px solid lightgrey;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(62, 62, 62)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}")
        self.btn_col1.setText("")
        self.btn_col1.setAutoRepeatDelay(305)
        self.btn_col1.setObjectName("btn_col1")
        self.horizontalLayout_22.addWidget(self.btn_col1)
        self.lbl_col = QtWidgets.QLabel(self.frame_coluse)
        self.lbl_col.setMinimumSize(QtCore.QSize(100, 30))
        self.lbl_col.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_col.setFont(font)
        self.lbl_col.setObjectName("lbl_col")
        self.horizontalLayout_22.addWidget(self.lbl_col)
        self.checkBox_use1 = QtWidgets.QCheckBox(self.frame_coluse)
        self.checkBox_use1.setMinimumSize(QtCore.QSize(30, 30))
        self.checkBox_use1.setMaximumSize(QtCore.QSize(30, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox_use1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_use1.setFont(font)
        self.checkBox_use1.setStyleSheet(" QCheckBox {\n"
"   spacing: 5px;\n"
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
"   image: url(:/resources//icons/24x24/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"   image: url(:/resources//icons/20x20/cil-task.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:pressed {\n"
"   image: url(:/resources//icons/16x16/cil-task.png);\n"
" }")
        self.checkBox_use1.setText("")
        self.checkBox_use1.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_use1.setCheckable(True)
        self.checkBox_use1.setChecked(False)
        self.checkBox_use1.setObjectName("checkBox_use1")
        self.horizontalLayout_22.addWidget(self.checkBox_use1)
        self.lbl_use = QtWidgets.QLabel(self.frame_coluse)
        self.lbl_use.setMinimumSize(QtCore.QSize(100, 30))
        self.lbl_use.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_use.setFont(font)
        self.lbl_use.setObjectName("lbl_use")
        self.horizontalLayout_22.addWidget(self.lbl_use)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem10)
        self.verticalLayout_16.addWidget(self.frame_coluse)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_45.addWidget(self.frame_10)
        self.verticalLayout_20.addWidget(self.frame_pltgroups)
        self.stackedWidget.addWidget(self.param_page)
        self.plot_page = QtWidgets.QWidget()
        self.plot_page.setObjectName("plot_page")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.plot_page)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_sidebar_plot = QtWidgets.QFrame(self.plot_page)
        self.frame_sidebar_plot.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_sidebar_plot.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_sidebar_plot.setStyleSheet("")
        self.frame_sidebar_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sidebar_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sidebar_plot.setObjectName("frame_sidebar_plot")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_sidebar_plot)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.btn_review = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_review.sizePolicy().hasHeightForWidth())
        self.btn_review.setSizePolicy(sizePolicy)
        self.btn_review.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_review.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_review.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_review.setFont(font)
        self.btn_review.setStyleSheet("QPushButton {    \n"
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
        self.btn_review.setAutoRepeatDelay(305)
        self.btn_review.setObjectName("btn_review")
        self.verticalLayout_14.addWidget(self.btn_review)
        self.btn_upset = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upset.sizePolicy().hasHeightForWidth())
        self.btn_upset.setSizePolicy(sizePolicy)
        self.btn_upset.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_upset.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_upset.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_upset.setFont(font)
        self.btn_upset.setStyleSheet("QPushButton {    \n"
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
        self.btn_upset.setAutoRepeatDelay(305)
        self.btn_upset.setObjectName("btn_upset")
        self.verticalLayout_14.addWidget(self.btn_upset)
        self.btn_dend = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dend.sizePolicy().hasHeightForWidth())
        self.btn_dend.setSizePolicy(sizePolicy)
        self.btn_dend.setMinimumSize(QtCore.QSize(121, 50))
        self.btn_dend.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_dend.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_dend.setFont(font)
        self.btn_dend.setStyleSheet("QPushButton {    \n"
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
        self.btn_dend.setAutoRepeatDelay(305)
        self.btn_dend.setObjectName("btn_dend")
        self.verticalLayout_14.addWidget(self.btn_dend)
        self.btn_pca = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pca.sizePolicy().hasHeightForWidth())
        self.btn_pca.setSizePolicy(sizePolicy)
        self.btn_pca.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_pca.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_pca.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_pca.setFont(font)
        self.btn_pca.setStyleSheet("QPushButton {    \n"
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
        self.btn_pca.setAutoRepeatDelay(305)
        self.btn_pca.setObjectName("btn_pca")
        self.verticalLayout_14.addWidget(self.btn_pca)
        self.btn_mzrt = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mzrt.sizePolicy().hasHeightForWidth())
        self.btn_mzrt.setSizePolicy(sizePolicy)
        self.btn_mzrt.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_mzrt.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_mzrt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_mzrt.setFont(font)
        self.btn_mzrt.setStyleSheet("QPushButton {    \n"
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
        self.btn_mzrt.setAutoRepeatDelay(305)
        self.btn_mzrt.setObjectName("btn_mzrt")
        self.verticalLayout_14.addWidget(self.btn_mzrt)
        self.btn_kmd = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_kmd.sizePolicy().hasHeightForWidth())
        self.btn_kmd.setSizePolicy(sizePolicy)
        self.btn_kmd.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_kmd.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_kmd.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_kmd.setFont(font)
        self.btn_kmd.setStyleSheet("QPushButton {    \n"
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
        self.btn_kmd.setAutoRepeatDelay(305)
        self.btn_kmd.setObjectName("btn_kmd")
        self.verticalLayout_14.addWidget(self.btn_kmd)
        self.btn_3dfc = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3dfc.sizePolicy().hasHeightForWidth())
        self.btn_3dfc.setSizePolicy(sizePolicy)
        self.btn_3dfc.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_3dfc.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_3dfc.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_3dfc.setFont(font)
        self.btn_3dfc.setStyleSheet("QPushButton {    \n"
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
        self.btn_3dfc.setAutoRepeatDelay(305)
        self.btn_3dfc.setObjectName("btn_3dfc")
        self.verticalLayout_14.addWidget(self.btn_3dfc)
        self.btn_volcano = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_volcano.sizePolicy().hasHeightForWidth())
        self.btn_volcano.setSizePolicy(sizePolicy)
        self.btn_volcano.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_volcano.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_volcano.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_volcano.setFont(font)
        self.btn_volcano.setStyleSheet("QPushButton {    \n"
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
        self.btn_volcano.setAutoRepeatDelay(305)
        self.btn_volcano.setObjectName("btn_volcano")
        self.verticalLayout_14.addWidget(self.btn_volcano)
        self.btn_heatmap = QtWidgets.QPushButton(self.frame_sidebar_plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_heatmap.sizePolicy().hasHeightForWidth())
        self.btn_heatmap.setSizePolicy(sizePolicy)
        self.btn_heatmap.setMinimumSize(QtCore.QSize(121, 75))
        self.btn_heatmap.setMaximumSize(QtCore.QSize(121, 75))
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
        self.btn_heatmap.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_heatmap.setFont(font)
        self.btn_heatmap.setStyleSheet("QPushButton {    \n"
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
        self.btn_heatmap.setAutoRepeatDelay(305)
        self.btn_heatmap.setObjectName("btn_heatmap")
        self.verticalLayout_14.addWidget(self.btn_heatmap)
        self.frame_sidebarspacer_2 = QtWidgets.QFrame(self.frame_sidebar_plot)
        self.frame_sidebarspacer_2.setMinimumSize(QtCore.QSize(121, 0))
        self.frame_sidebarspacer_2.setMaximumSize(QtCore.QSize(121, 16777215))
        self.frame_sidebarspacer_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.frame_sidebarspacer_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sidebarspacer_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sidebarspacer_2.setObjectName("frame_sidebarspacer_2")
        self.verticalLayout_14.addWidget(self.frame_sidebarspacer_2)
        self.horizontalLayout_9.addWidget(self.frame_sidebar_plot)
        self.frame_plots = QtWidgets.QFrame(self.plot_page)
        self.frame_plots.setStyleSheet("background-color: rgba(225,225,225,255);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_plots.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plots.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plots.setObjectName("frame_plots")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_plots)
        self.verticalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.stackedWidget_plot = QtWidgets.QStackedWidget(self.frame_plots)
        self.stackedWidget_plot.setStyleSheet("")
        self.stackedWidget_plot.setObjectName("stackedWidget_plot")
        self.page_logo2 = QtWidgets.QWidget()
        self.page_logo2.setStyleSheet("background-image: url(:/resources/icons/logodark.png);")
        self.page_logo2.setObjectName("page_logo2")
        self.stackedWidget_plot.addWidget(self.page_logo2)
        self.page_feature = QtWidgets.QWidget()
        self.page_feature.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.page_feature.setObjectName("page_feature")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.page_feature)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.frame_5 = QtWidgets.QFrame(self.page_feature)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.btn_datasummary = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_datasummary.sizePolicy().hasHeightForWidth())
        self.btn_datasummary.setSizePolicy(sizePolicy)
        self.btn_datasummary.setMinimumSize(QtCore.QSize(125, 40))
        self.btn_datasummary.setMaximumSize(QtCore.QSize(125, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_datasummary.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_datasummary.setFont(font)
        self.btn_datasummary.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(212,212,212, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175,175,175)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150,150,150);\n"
"}")
        self.btn_datasummary.setAutoRepeatDelay(305)
        self.btn_datasummary.setObjectName("btn_datasummary")
        self.horizontalLayout_18.addWidget(self.btn_datasummary)
        self.btn_ftrplt = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ftrplt.sizePolicy().hasHeightForWidth())
        self.btn_ftrplt.setSizePolicy(sizePolicy)
        self.btn_ftrplt.setMinimumSize(QtCore.QSize(125, 40))
        self.btn_ftrplt.setMaximumSize(QtCore.QSize(125, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_ftrplt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ftrplt.setFont(font)
        self.btn_ftrplt.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(212,212,212, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175,175,175)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150,150,150);\n"
"}")
        self.btn_ftrplt.setAutoRepeatDelay(305)
        self.btn_ftrplt.setObjectName("btn_ftrplt")
        self.horizontalLayout_18.addWidget(self.btn_ftrplt)
        self.btn_treemap = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_treemap.sizePolicy().hasHeightForWidth())
        self.btn_treemap.setSizePolicy(sizePolicy)
        self.btn_treemap.setMinimumSize(QtCore.QSize(125, 40))
        self.btn_treemap.setMaximumSize(QtCore.QSize(125, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_treemap.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_treemap.setFont(font)
        self.btn_treemap.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(212,212,212, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175,175,175)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150,150,150);\n"
"}")
        self.btn_treemap.setAutoRepeatDelay(305)
        self.btn_treemap.setObjectName("btn_treemap")
        self.horizontalLayout_18.addWidget(self.btn_treemap)
        self.btn_cvplt = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cvplt.sizePolicy().hasHeightForWidth())
        self.btn_cvplt.setSizePolicy(sizePolicy)
        self.btn_cvplt.setMinimumSize(QtCore.QSize(125, 40))
        self.btn_cvplt.setMaximumSize(QtCore.QSize(125, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_cvplt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cvplt.setFont(font)
        self.btn_cvplt.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(212,212,212, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175,175,175)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150,150,150);\n"
"}")
        self.btn_cvplt.setAutoRepeatDelay(305)
        self.btn_cvplt.setObjectName("btn_cvplt")
        self.horizontalLayout_18.addWidget(self.btn_cvplt)
        self.verticalLayout_42.addWidget(self.frame_5)
        self.stackedWidget_review = QtWidgets.QStackedWidget(self.page_feature)
        self.stackedWidget_review.setObjectName("stackedWidget_review")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_24.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_featureplt = QtWidgets.QFrame(self.page_2)
        self.frame_featureplt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_featureplt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_featureplt.setObjectName("frame_featureplt")
        self.verticalLayout_24.addWidget(self.frame_featureplt)
        self.stackedWidget_review.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_43.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.frame_treemap = QtWidgets.QFrame(self.page_3)
        self.frame_treemap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_treemap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_treemap.setObjectName("frame_treemap")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_treemap)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem11 = QtWidgets.QSpacerItem(365, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem11)
        self.label_treemap = QtWidgets.QLabel(self.frame_treemap)
        self.label_treemap.setText("")
        self.label_treemap.setObjectName("label_treemap")
        self.horizontalLayout_20.addWidget(self.label_treemap)
        spacerItem12 = QtWidgets.QSpacerItem(364, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.verticalLayout_43.addWidget(self.frame_treemap)
        self.stackedWidget_review.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_44.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.frame_cvplt = QtWidgets.QFrame(self.page_4)
        self.frame_cvplt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cvplt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cvplt.setObjectName("frame_cvplt")
        self.verticalLayout_44.addWidget(self.frame_cvplt)
        self.stackedWidget_review.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_cvplt_2 = QtWidgets.QFrame(self.page_5)
        self.frame_cvplt_2.setMinimumSize(QtCore.QSize(420, 0))
        self.frame_cvplt_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cvplt_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cvplt_2.setObjectName("frame_cvplt_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_cvplt_2)
        self.verticalLayout_26.setContentsMargins(20, 0, 13, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.lbl_spllist_2 = QtWidgets.QLabel(self.frame_cvplt_2)
        self.lbl_spllist_2.setMinimumSize(QtCore.QSize(200, 50))
        self.lbl_spllist_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_spllist_2.setFont(font)
        self.lbl_spllist_2.setStyleSheet("color : rgb(70, 70, 70)")
        self.lbl_spllist_2.setObjectName("lbl_spllist_2")
        self.verticalLayout_26.addWidget(self.lbl_spllist_2)
        self.frame_7 = QtWidgets.QFrame(self.frame_cvplt_2)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.lbl_spllist_3 = QtWidgets.QLabel(self.frame_7)
        self.lbl_spllist_3.setMinimumSize(QtCore.QSize(140, 40))
        self.lbl_spllist_3.setMaximumSize(QtCore.QSize(140, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_spllist_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_spllist_3.setFont(font)
        self.lbl_spllist_3.setStyleSheet("color : rgb(70, 70, 70)")
        self.lbl_spllist_3.setObjectName("lbl_spllist_3")
        self.verticalLayout_28.addWidget(self.lbl_spllist_3)
        self.verticalLayout_26.addWidget(self.frame_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem13)
        self.horizontalLayout_19.addWidget(self.frame_cvplt_2)
        self.textBrowser_mp_prev = QtWidgets.QTextBrowser(self.page_5)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
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
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textBrowser_mp_prev.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_mp_prev.setFont(font)
        self.textBrowser_mp_prev.setStyleSheet("QTextBrowser{\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QScrollBar:vertical {\n"
"            border: 1px solid #555555;\n"
"            border-radius: 2px;\n"
"            background: rgb(70,70,70);\n"
"            width:20px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            border-radius: 2px;\n"
"            background-color: rgb(50,50,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.textBrowser_mp_prev.setObjectName("textBrowser_mp_prev")
        self.horizontalLayout_19.addWidget(self.textBrowser_mp_prev)
        self.stackedWidget_review.addWidget(self.page_5)
        self.verticalLayout_42.addWidget(self.stackedWidget_review)
        self.stackedWidget_plot.addWidget(self.page_feature)
        self.page_dend = QtWidgets.QWidget()
        self.page_dend.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.page_dend.setObjectName("page_dend")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.page_dend)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.frame_dend = QtWidgets.QFrame(self.page_dend)
        self.frame_dend.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dend.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dend.setObjectName("frame_dend")
        self.verticalLayout_31.addWidget(self.frame_dend)
        self.stackedWidget_plot.addWidget(self.page_dend)
        self.page_pca = QtWidgets.QWidget()
        self.page_pca.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.page_pca.setObjectName("page_pca")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.page_pca)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_pca = QtWidgets.QFrame(self.page_pca)
        self.frame_pca.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pca.setObjectName("frame_pca")
        self.verticalLayout_30.addWidget(self.frame_pca)
        self.stackedWidget_plot.addWidget(self.page_pca)
        self.page_mzrt = QtWidgets.QWidget()
        self.page_mzrt.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.page_mzrt.setObjectName("page_mzrt")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_mzrt)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_mzrt = QtWidgets.QFrame(self.page_mzrt)
        self.frame_mzrt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mzrt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mzrt.setObjectName("frame_mzrt")
        self.verticalLayout_17.addWidget(self.frame_mzrt)
        self.stackedWidget_plot.addWidget(self.page_mzrt)
        self.page_kmd = QtWidgets.QWidget()
        self.page_kmd.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.page_kmd.setObjectName("page_kmd")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.page_kmd)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_kmd = QtWidgets.QFrame(self.page_kmd)
        self.frame_kmd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_kmd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_kmd.setObjectName("frame_kmd")
        self.verticalLayout_34.addWidget(self.frame_kmd)
        self.stackedWidget_plot.addWidget(self.page_kmd)
        self.page_3dfc = QtWidgets.QWidget()
        self.page_3dfc.setObjectName("page_3dfc")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.page_3dfc)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.frame_fc3d = QtWidgets.QFrame(self.page_3dfc)
        self.frame_fc3d.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_fc3d.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fc3d.setObjectName("frame_fc3d")
        self.verticalLayout_33.addWidget(self.frame_fc3d)
        self.stackedWidget_plot.addWidget(self.page_3dfc)
        self.page_volcano = QtWidgets.QWidget()
        self.page_volcano.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.page_volcano.setObjectName("page_volcano")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page_volcano)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lbl_volcanowarn = QtWidgets.QLabel(self.page_volcano)
        self.lbl_volcanowarn.setMinimumSize(QtCore.QSize(250, 20))
        self.lbl_volcanowarn.setMaximumSize(QtCore.QSize(16777215, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(110, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_volcanowarn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_volcanowarn.setFont(font)
        self.lbl_volcanowarn.setText("")
        self.lbl_volcanowarn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_volcanowarn.setObjectName("lbl_volcanowarn")
        self.verticalLayout_19.addWidget(self.lbl_volcanowarn)
        self.frame_volcano = QtWidgets.QFrame(self.page_volcano)
        self.frame_volcano.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_volcano.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_volcano.setObjectName("frame_volcano")
        self.verticalLayout_19.addWidget(self.frame_volcano)
        self.stackedWidget_plot.addWidget(self.page_volcano)
        self.page_heatmap = QtWidgets.QWidget()
        self.page_heatmap.setObjectName("page_heatmap")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.page_heatmap)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_heatmap = QtWidgets.QFrame(self.page_heatmap)
        self.frame_heatmap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_heatmap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_heatmap.setObjectName("frame_heatmap")
        self.verticalLayout_35.addWidget(self.frame_heatmap)
        self.stackedWidget_plot.addWidget(self.page_heatmap)
        self.page_sets = QtWidgets.QWidget()
        self.page_sets.setObjectName("page_sets")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_sets)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_12 = QtWidgets.QFrame(self.page_sets)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.btn_upsetplt = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upsetplt.sizePolicy().hasHeightForWidth())
        self.btn_upsetplt.setSizePolicy(sizePolicy)
        self.btn_upsetplt.setMinimumSize(QtCore.QSize(125, 40))
        self.btn_upsetplt.setMaximumSize(QtCore.QSize(125, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_upsetplt.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_upsetplt.setFont(font)
        self.btn_upsetplt.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(212,212,212, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175,175,175)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150,150,150);\n"
"}")
        self.btn_upsetplt.setAutoRepeatDelay(305)
        self.btn_upsetplt.setObjectName("btn_upsetplt")
        self.horizontalLayout_25.addWidget(self.btn_upsetplt)
        self.btn_samplecorr = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_samplecorr.sizePolicy().hasHeightForWidth())
        self.btn_samplecorr.setSizePolicy(sizePolicy)
        self.btn_samplecorr.setMinimumSize(QtCore.QSize(200, 40))
        self.btn_samplecorr.setMaximumSize(QtCore.QSize(200, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_samplecorr.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_samplecorr.setFont(font)
        self.btn_samplecorr.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(212,212,212, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175,175,175)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150,150,150);\n"
"}")
        self.btn_samplecorr.setAutoRepeatDelay(305)
        self.btn_samplecorr.setObjectName("btn_samplecorr")
        self.horizontalLayout_25.addWidget(self.btn_samplecorr)
        self.verticalLayout_11.addWidget(self.frame_12)
        self.stackedWidget_grpanalysis = QtWidgets.QStackedWidget(self.page_sets)
        self.stackedWidget_grpanalysis.setObjectName("stackedWidget_grpanalysis")
        self.page_upset = QtWidgets.QWidget()
        self.page_upset.setObjectName("page_upset")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_upset)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_upset = QtWidgets.QFrame(self.page_upset)
        self.frame_upset.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_upset.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_upset.setObjectName("frame_upset")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_upset)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.label_upset = QtWidgets.QLabel(self.frame_upset)
        self.label_upset.setText("")
        self.label_upset.setObjectName("label_upset")
        self.verticalLayout_41.addWidget(self.label_upset)
        self.verticalLayout_15.addWidget(self.frame_upset)
        self.stackedWidget_grpanalysis.addWidget(self.page_upset)
        self.page_samplecorr = QtWidgets.QWidget()
        self.page_samplecorr.setObjectName("page_samplecorr")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.page_samplecorr)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_samplecorr = QtWidgets.QFrame(self.page_samplecorr)
        self.frame_samplecorr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_samplecorr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_samplecorr.setObjectName("frame_samplecorr")
        self.verticalLayout_25.addWidget(self.frame_samplecorr)
        self.stackedWidget_grpanalysis.addWidget(self.page_samplecorr)
        self.verticalLayout_11.addWidget(self.stackedWidget_grpanalysis)
        self.stackedWidget_plot.addWidget(self.page_sets)
        self.verticalLayout_23.addWidget(self.stackedWidget_plot)
        self.stackedWidget_infobar = QtWidgets.QStackedWidget(self.frame_plots)
        self.stackedWidget_infobar.setMinimumSize(QtCore.QSize(0, 40))
        self.stackedWidget_infobar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.stackedWidget_infobar.setObjectName("stackedWidget_infobar")
        self.page_featureinfo = QtWidgets.QWidget()
        self.page_featureinfo.setMinimumSize(QtCore.QSize(0, 40))
        self.page_featureinfo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.page_featureinfo.setObjectName("page_featureinfo")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.page_featureinfo)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.frame_featureinfo = QtWidgets.QFrame(self.page_featureinfo)
        self.frame_featureinfo.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_featureinfo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_featureinfo.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_featureinfo.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.frame_featureinfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_featureinfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_featureinfo.setObjectName("frame_featureinfo")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_featureinfo)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_featurename = QtWidgets.QLabel(self.frame_featureinfo)
        self.lbl_featurename.setMinimumSize(QtCore.QSize(250, 40))
        self.lbl_featurename.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_featurename.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_featurename.setFont(font)
        self.lbl_featurename.setObjectName("lbl_featurename")
        self.horizontalLayout_10.addWidget(self.lbl_featurename)
        self.lbl_featurert = QtWidgets.QLabel(self.frame_featureinfo)
        self.lbl_featurert.setMinimumSize(QtCore.QSize(200, 40))
        self.lbl_featurert.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_featurert.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_featurert.setFont(font)
        self.lbl_featurert.setText("")
        self.lbl_featurert.setObjectName("lbl_featurert")
        self.horizontalLayout_10.addWidget(self.lbl_featurert)
        self.lbl_featuremz = QtWidgets.QLabel(self.frame_featureinfo)
        self.lbl_featuremz.setMinimumSize(QtCore.QSize(150, 40))
        self.lbl_featuremz.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_featuremz.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_featuremz.setFont(font)
        self.lbl_featuremz.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.lbl_featuremz.setText("")
        self.lbl_featuremz.setObjectName("lbl_featuremz")
        self.horizontalLayout_10.addWidget(self.lbl_featuremz)
        self.btn_details = QtWidgets.QPushButton(self.frame_featureinfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_details.sizePolicy().hasHeightForWidth())
        self.btn_details.setSizePolicy(sizePolicy)
        self.btn_details.setMinimumSize(QtCore.QSize(125, 40))
        self.btn_details.setMaximumSize(QtCore.QSize(125, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_details.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_details.setFont(font)
        self.btn_details.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(212,212,212, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(175,175,175)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(150,150,150);\n"
"}")
        self.btn_details.setAutoRepeatDelay(305)
        self.btn_details.setObjectName("btn_details")
        self.horizontalLayout_10.addWidget(self.btn_details)
        self.verticalLayout_32.addWidget(self.frame_featureinfo)
        self.stackedWidget_infobar.addWidget(self.page_featureinfo)
        self.page_sampleinfo = QtWidgets.QWidget()
        self.page_sampleinfo.setObjectName("page_sampleinfo")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.page_sampleinfo)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lbl_injname = QtWidgets.QLabel(self.page_sampleinfo)
        self.lbl_injname.setMinimumSize(QtCore.QSize(250, 40))
        self.lbl_injname.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_injname.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_injname.setFont(font)
        self.lbl_injname.setObjectName("lbl_injname")
        self.horizontalLayout_17.addWidget(self.lbl_injname)
        self.lbl_sample = QtWidgets.QLabel(self.page_sampleinfo)
        self.lbl_sample.setMinimumSize(QtCore.QSize(150, 40))
        self.lbl_sample.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_sample.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sample.setFont(font)
        self.lbl_sample.setStyleSheet("background-color: rgba(225,225,225,255)")
        self.lbl_sample.setText("")
        self.lbl_sample.setObjectName("lbl_sample")
        self.horizontalLayout_17.addWidget(self.lbl_sample)
        self.lbl_biolgrp = QtWidgets.QLabel(self.page_sampleinfo)
        self.lbl_biolgrp.setMinimumSize(QtCore.QSize(200, 40))
        self.lbl_biolgrp.setMaximumSize(QtCore.QSize(16777215, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(75, 75, 75))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_biolgrp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_biolgrp.setFont(font)
        self.lbl_biolgrp.setText("")
        self.lbl_biolgrp.setObjectName("lbl_biolgrp")
        self.horizontalLayout_17.addWidget(self.lbl_biolgrp)
        self.stackedWidget_infobar.addWidget(self.page_sampleinfo)
        self.verticalLayout_23.addWidget(self.stackedWidget_infobar)
        self.horizontalLayout_9.addWidget(self.frame_plots)
        self.stackedWidget.addWidget(self.plot_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.info_page)
        self.verticalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_info = QtWidgets.QFrame(self.info_page)
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_info)
        self.horizontalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_info = QtWidgets.QTextBrowser(self.frame_info)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
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
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textBrowser_info.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_info.setFont(font)
        self.textBrowser_info.setStyleSheet("QTextBrowser{\n"
"    background-color: rgba(0,0,0,0);\n"
"    border: 0;\n"
"}\n"
"QScrollBar:vertical {\n"
"            border: 1px solid #555555;\n"
"            border-radius: 2px;\n"
"            background: rgb(70,70,70);\n"
"            width:30px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            border-radius: 2px;\n"
"            background-color: rgb(50,50,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.textBrowser_info.setObjectName("textBrowser_info")
        self.horizontalLayout_4.addWidget(self.textBrowser_info)
        self.verticalLayout_4.addWidget(self.frame_info)
        self.stackedWidget.addWidget(self.info_page)
        self.search_page = QtWidgets.QWidget()
        self.search_page.setObjectName("search_page")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.search_page)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame = QtWidgets.QFrame(self.search_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setMinimumSize(QtCore.QSize(200, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 70, 70, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.treeWidget.setPalette(palette)
        self.treeWidget.setStyleSheet("QTreeView {\n"
"    border-top: 2px solid rgb(70,70,70);\n"
"    border-bottom: 1px solid rgb(70,70,70);\n"
"    border-left: 1px solid rgb(70,70,70);\n"
"    border-right: 1px solid rgb(70,70,70);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(200,200,200,30);\n"
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
"    color: rgb(200,200,200);\n"
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
"            width:20px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"            background: none;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-width: 0px;\n"
"              border: 2px rgb(40,40,40);\n"
"            border-radius: 2px;\n"
"            background-color: rgb(50,50,50);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"QTreeView::hideColumn(3)\n"
"")
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_39.addWidget(self.treeWidget)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.frame_blankfil_params4_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_blankfil_params4_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_blankfil_params4_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_blankfil_params4_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_blankfil_params4_2.setObjectName("frame_blankfil_params4_2")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_blankfil_params4_2)
        self.horizontalLayout_24.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.lbl_blankfil_ppmthresh = QtWidgets.QLabel(self.frame_blankfil_params4_2)
        self.lbl_blankfil_ppmthresh.setMinimumSize(QtCore.QSize(225, 40))
        self.lbl_blankfil_ppmthresh.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_blankfil_ppmthresh.setFont(font)
        self.lbl_blankfil_ppmthresh.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_blankfil_ppmthresh.setObjectName("lbl_blankfil_ppmthresh")
        self.horizontalLayout_24.addWidget(self.lbl_blankfil_ppmthresh)
        self.lineEdit_ppmthresh = QtWidgets.QLineEdit(self.frame_blankfil_params4_2)
        self.lineEdit_ppmthresh.setMinimumSize(QtCore.QSize(150, 30))
        self.lineEdit_ppmthresh.setMaximumSize(QtCore.QSize(150, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.lineEdit_ppmthresh.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(-1)
        self.lineEdit_ppmthresh.setFont(font)
        self.lineEdit_ppmthresh.setStyleSheet("QLineEdit{ \n"
"    background-color:rgba(0,0,0,0);\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: rgba(0,0,0,0);\n"
"    font-size: 18px;\n"
"    font-family: Bahnschrift SemiBold\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color:rgba(0,0,0,0);\n"
"}")
        self.lineEdit_ppmthresh.setObjectName("lineEdit_ppmthresh")
        self.horizontalLayout_24.addWidget(self.lineEdit_ppmthresh)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem14)
        self.btn_details_2 = QtWidgets.QPushButton(self.frame_blankfil_params4_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_details_2.sizePolicy().hasHeightForWidth())
        self.btn_details_2.setSizePolicy(sizePolicy)
        self.btn_details_2.setMinimumSize(QtCore.QSize(125, 40))
        self.btn_details_2.setMaximumSize(QtCore.QSize(125, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btn_details_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_details_2.setFont(font)
        self.btn_details_2.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: rgba(40,40,40, 255)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50,50,50)\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(60,60,60);\n"
"}")
        self.btn_details_2.setAutoRepeatDelay(305)
        self.btn_details_2.setObjectName("btn_details_2")
        self.horizontalLayout_24.addWidget(self.btn_details_2)
        self.verticalLayout_38.addWidget(self.frame_blankfil_params4_2)
        self.verticalLayout_39.addWidget(self.frame_4)
        self.verticalLayout_36.addWidget(self.frame)
        self.stackedWidget.addWidget(self.search_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setStyleSheet("background: transparent;\n"
"background-image: url(:/resources/icons/logogrey.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.stackedWidget.addWidget(self.page)
        self.verticalLayout_18.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.content_bar)
        self.verticalLayout.addWidget(self.drop_shadow_frame)
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
        self.frame_label_credits.setMaximumSize(QtCore.QSize(125, 16777215))
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
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_27.addWidget(self.label_credits)
        self.horizontalLayout_15.addWidget(self.frame_label_credits)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.label_status = QtWidgets.QLabel(self.credits_bar)
        self.label_status.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color: rgb(150,150,150);")
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_15.addWidget(self.label_status)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem16)
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
        self.stackedWidget_plot.setCurrentIndex(7)
        self.stackedWidget_review.setCurrentIndex(0)
        self.stackedWidget_grpanalysis.setCurrentIndex(1)
        self.stackedWidget_infobar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_import, self.btn_filter)
        MainWindow.setTabOrder(self.btn_filter, self.btn_parameters)
        MainWindow.setTabOrder(self.btn_parameters, self.btn_plots)
        MainWindow.setTabOrder(self.btn_plots, self.btn_info)
        MainWindow.setTabOrder(self.btn_info, self.btn_import_pktbl)
        MainWindow.setTabOrder(self.btn_import_pktbl, self.btn_import_spllist)
        MainWindow.setTabOrder(self.btn_import_spllist, self.btn_import_splmdt)
        MainWindow.setTabOrder(self.btn_import_splmdt, self.btn_import_outdir)
        MainWindow.setTabOrder(self.btn_import_outdir, self.radioButton_meancv)
        MainWindow.setTabOrder(self.radioButton_meancv, self.lineEdit_cvthresh)
        MainWindow.setTabOrder(self.lineEdit_cvthresh, self.checkBox_fc)
        MainWindow.setTabOrder(self.checkBox_fc, self.checkBox_ttest)
        MainWindow.setTabOrder(self.checkBox_ttest, self.checkBox_pca)
        MainWindow.setTabOrder(self.checkBox_pca, self.checkBox_dend)
        MainWindow.setTabOrder(self.checkBox_dend, self.checkBox_mzrt)
        MainWindow.setTabOrder(self.checkBox_mzrt, self.checkBox_kmd)
        MainWindow.setTabOrder(self.checkBox_kmd, self.checkBox_3dfc)
        MainWindow.setTabOrder(self.checkBox_3dfc, self.checkBox_volcano)
        MainWindow.setTabOrder(self.checkBox_volcano, self.textBrowser_info)
        MainWindow.setTabOrder(self.textBrowser_info, self.btn_minimize)
        MainWindow.setTabOrder(self.btn_minimize, self.btn_maximize)
        MainWindow.setTabOrder(self.btn_maximize, self.btn_close)
        MainWindow.setTabOrder(self.btn_close, self.btn_run)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">MPACT</span></p></body></html>"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.btn_import.setToolTip(_translate("MainWindow", "Import"))
        self.btn_filter.setToolTip(_translate("MainWindow", "Filtering and Error Correction"))
        self.btn_parameters.setToolTip(_translate("MainWindow", "Analysis Parameters"))
        self.btn_plots.setToolTip(_translate("MainWindow", "Data Visualization"))
        self.btn_search.setToolTip(_translate("MainWindow", "Analysis Info"))
        self.btn_info.setToolTip(_translate("MainWindow", "Analysis Info"))
        self.btn_run.setToolTip(_translate("MainWindow", "Run Analysis"))
        self.lbl_splmdt_2.setText(_translate("MainWindow", "<html><head/><body><p>File Selection</p></body></html>"))
        self.btn_load_session.setToolTip(_translate("MainWindow", "Import"))
        self.btn_load_session.setText(_translate("MainWindow", "Import from .MCPT session file"))
        self.btn_import_pktbl.setToolTip(_translate("MainWindow", "Import"))
        self.btn_import_pktbl.setText(_translate("MainWindow", "Peak Table            "))
        self.btn_import_spllist.setToolTip(_translate("MainWindow", "Import"))
        self.btn_import_spllist.setText(_translate("MainWindow", "Sample List          "))
        self.btn_import_splmdt.setToolTip(_translate("MainWindow", "Import"))
        self.btn_import_splmdt.setText(_translate("MainWindow", "Sample Metadata"))
        self.btn_import_msp.setToolTip(_translate("MainWindow", "Import"))
        self.btn_import_msp.setText(_translate("MainWindow", "Fragment Database"))
        self.btn_import_outdir.setToolTip(_translate("MainWindow", "Import"))
        self.btn_import_outdir.setText(_translate("MainWindow", "Output Directory "))
        self.lbl_pktbl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">None Selected</span></p></body></html>"))
        self.lbl_spllist.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">None Selected</span></p></body></html>"))
        self.lbl_splmdt.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">None Selected</span></p></body></html>"))
        self.lbl_msp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">None Selected (optional)</span></p></body></html>"))
        self.lbl_outdir.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">None Selected</span></p></body></html>"))
        self.checkBox_mp.setText(_translate("MainWindow", "Mispicked Peak Correction"))
        self.checkBox_merge.setText(_translate("MainWindow", "Merge Peaks"))
        self.lineEdit_ringwin.setText(_translate("MainWindow", "0.5"))
        self.combo_maxisoshift.setItemText(0, _translate("MainWindow", "0"))
        self.combo_maxisoshift.setItemText(1, _translate("MainWindow", "1"))
        self.combo_maxisoshift.setItemText(2, _translate("MainWindow", "2"))
        self.combo_maxisoshift.setItemText(3, _translate("MainWindow", "3"))
        self.combo_maxisoshift.setItemText(4, _translate("MainWindow", "4"))
        self.combo_maxisoshift.setItemText(5, _translate("MainWindow", "5"))
        self.lbl_ringwin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Ringing Mass Window</span></p></body></html>"))
        self.lineEdit_isowin.setText(_translate("MainWindow", "0.01"))
        self.lbl_isowin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Isotope Mass Window</span></p></body></html>"))
        self.lineEdit_rtwin.setText(_translate("MainWindow", "0.005"))
        self.lbl_maxisoshift.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Max Isotopic Mass Shift</span></p></body></html>"))
        self.lbl_rtwin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#d4d4d4;\">t</span><span style=\" font-style:italic; color:#d4d4d4; vertical-align:sub;\">R</span><span style=\" color:#d4d4d4;\"> Window</span></p></body></html>"))
        self.checkBox_blankfilter.setText(_translate("MainWindow", "Solvent Blank Filtering"))
        self.lbl_blankfil_name_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Blank Code</span></p></body></html>"))
        self.checkBox_cv.setText(_translate("MainWindow", "CV Filter"))
        self.radioButton_meancv.setText(_translate("MainWindow", "Mean CV"))
        self.lbl_cvthresh.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">CV Threshold</span></p><p><br/></p></body></html>"))
        self.lineEdit_cvthresh.setText(_translate("MainWindow", "0.2"))
        self.radioButton_medcv.setText(_translate("MainWindow", "Median CV"))
        self.checkBox_decon.setText(_translate("MainWindow", "Insource Ion Filter"))
        self.lbl_insourcethresh.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bfbfbf;\">Threshold</span></p></body></html>"))
        self.lineEdit_insourcethresh.setText(_translate("MainWindow", "0.95"))
        self.lbl_grpprs_2.setText(_translate("MainWindow", "<html><head/><body><p>Group Parsing</p></body></html>"))
        self.radioButton_blankfilter_abs.setText(_translate("MainWindow", "Absolute Theshold"))
        self.lineEdit_blankfilter_relthresh.setText(_translate("MainWindow", "0.01"))
        self.lineEdit_blankfilter_absthresh.setText(_translate("MainWindow", "100"))
        self.radioButton_blankfilter_rel.setText(_translate("MainWindow", "Relative Threshold"))
        self.lbl_calc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Calculations</span></p></body></html>"))
        self.checkBox_fc.setText(_translate("MainWindow", "Fold Change"))
        self.checkBox_ttest.setText(_translate("MainWindow", "T test"))
        self.lbl_expgrp.setText(_translate("MainWindow", "<html><head/><body><p>Experimental Group</p></body></html>"))
        self.checkBox_FDR.setText(_translate("MainWindow", "FDR Correction"))
        self.lbl_ctrgrp.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Control Group</span></p></body></html>"))
        self.lbl_plotparams.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Plots</span></p></body></html>"))
        self.checkBox_pca.setText(_translate("MainWindow", "PCA"))
        self.checkBox_dend.setText(_translate("MainWindow", "Dendrogram"))
        self.checkBox_mzrt.setText(_translate("MainWindow", "m/z vs RT"))
        self.checkBox_kmd.setText(_translate("MainWindow", "Mass Defect"))
        self.checkBox_3dfc.setText(_translate("MainWindow", "3D Fold Change"))
        self.checkBox_volcano.setText(_translate("MainWindow", "Volcano Plot"))
        self.lbl_pltgroups.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Plot Feature Sets</span></p></body></html>"))
        self.btn_addgroup.setToolTip(_translate("MainWindow", "Import"))
        self.btn_removegroup.setToolTip(_translate("MainWindow", "Import"))
        self.lbl_calc_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Available Groups</span></p></body></html>"))
        self.lbl_calc_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">May be in:</span></p></body></html>"))
        self.lbl_calc_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Must be in:</span></p></body></html>"))
        self.btn_col1.setToolTip(_translate("MainWindow", "Import"))
        self.lbl_col.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Color</span></p></body></html>"))
        self.lbl_use.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">Use</span></p></body></html>"))
        self.btn_review.setToolTip(_translate("MainWindow", "Data Review Raw Feature Plot"))
        self.btn_review.setText(_translate("MainWindow", "Data Review"))
        self.btn_upset.setToolTip(_translate("MainWindow", "Volcano Plot"))
        self.btn_upset.setText(_translate("MainWindow", "Group Analysis"))
        self.btn_dend.setToolTip(_translate("MainWindow", "Heirarchal Clustering Dendrogram"))
        self.btn_dend.setText(_translate("MainWindow", "Dendrogram"))
        self.btn_pca.setToolTip(_translate("MainWindow", "Principal Component Analysis"))
        self.btn_pca.setText(_translate("MainWindow", "Multivariate"))
        self.btn_mzrt.setToolTip(_translate("MainWindow", "m/z vs RT Feature Plot by Group Set"))
        self.btn_mzrt.setText(_translate("MainWindow", "m/z vs RT"))
        self.btn_kmd.setToolTip(_translate("MainWindow", "Kendrick Mass Defect vs Nominal Mass"))
        self.btn_kmd.setText(_translate("MainWindow", "KMD"))
        self.btn_3dfc.setToolTip(_translate("MainWindow", "3D Fold Change vs m/z vs RT"))
        self.btn_3dfc.setText(_translate("MainWindow", "3D FC"))
        self.btn_volcano.setToolTip(_translate("MainWindow", "Volcano Plot"))
        self.btn_volcano.setText(_translate("MainWindow", "Volcano"))
        self.btn_heatmap.setToolTip(_translate("MainWindow", "Volcano Plot"))
        self.btn_heatmap.setText(_translate("MainWindow", "Heatmap"))
        self.btn_datasummary.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_datasummary.setText(_translate("MainWindow", "Summary"))
        self.btn_ftrplt.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_ftrplt.setText(_translate("MainWindow", "Feature plot"))
        self.btn_treemap.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_treemap.setText(_translate("MainWindow", "Tree map"))
        self.btn_cvplt.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_cvplt.setText(_translate("MainWindow", "CV plot"))
        self.lbl_spllist_2.setText(_translate("MainWindow", "<html><head/><body><p>Data Quality</p></body></html>"))
        self.lbl_spllist_3.setText(_translate("MainWindow", "<html><head/><body><p>Overall: --%</p></body></html>"))
        self.textBrowser_mp_prev.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift SemiBold\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_upsetplt.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_upsetplt.setText(_translate("MainWindow", "Sets"))
        self.btn_samplecorr.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_samplecorr.setText(_translate("MainWindow", "Sample Correlations"))
        self.lbl_featurename.setText(_translate("MainWindow", "No Feature Selected"))
        self.btn_details.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_details.setText(_translate("MainWindow", "Details"))
        self.lbl_injname.setText(_translate("MainWindow", "No Sample Selected"))
        self.textBrowser_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift SemiBold\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Compound"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "m/z"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "TR"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Groups"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "FC"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Hits"))
        self.lbl_blankfil_ppmthresh.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d4d4d4;\">PPM Theshold</span></p></body></html>"))
        self.lineEdit_ppmthresh.setText(_translate("MainWindow", "10"))
        self.btn_details_2.setToolTip(_translate("MainWindow", "View Feature Details"))
        self.btn_details_2.setText(_translate("MainWindow", "Details"))
        self.label_credits.setText(_translate("MainWindow", "Rev 21.05.03"))
        self.label_status.setText(_translate("MainWindow", "Idle"))

import files_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

