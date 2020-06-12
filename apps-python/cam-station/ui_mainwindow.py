# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDockNestingEnabled(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.videoPreview = QtWidgets.QLabel(self.centralWidget)
        self.videoPreview.setGeometry(QtCore.QRect(0, 0, 960, 540))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoPreview.sizePolicy().hasHeightForWidth())
        self.videoPreview.setSizePolicy(sizePolicy)
        self.videoPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.videoPreview.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.videoPreview.setMidLineWidth(1)
        self.videoPreview.setObjectName("videoPreview")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(970, 10, 300, 171))
        self.groupBox.setObjectName("groupBox")
        self.pushBtn_Video = QtWidgets.QPushButton(self.groupBox)
        self.pushBtn_Video.setGeometry(QtCore.QRect(10, 90, 281, 40))
        self.pushBtn_Video.setCheckable(False)
        self.pushBtn_Video.setObjectName("pushBtn_Video")
        self.check_proc = QtWidgets.QCheckBox(self.groupBox)
        self.check_proc.setGeometry(QtCore.QRect(10, 130, 110, 40))
        self.check_proc.setObjectName("check_proc")
        self.box_cam = QtWidgets.QComboBox(self.groupBox)
        self.box_cam.setGeometry(QtCore.QRect(10, 30, 70, 51))
        self.box_cam.setObjectName("box_cam")
        self.box_cam.addItem("")
        self.box_cam.addItem("")
        self.box_cam.addItem("")
        self.box_cam.addItem("")
        self.box_loc = QtWidgets.QTextEdit(self.groupBox)
        self.box_loc.setGeometry(QtCore.QRect(90, 30, 200, 51))
        self.box_loc.setObjectName("box_loc")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(970, 540, 300, 190))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushBtn_Map = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtn_Map.setGeometry(QtCore.QRect(10, 140, 281, 40))
        self.pushBtn_Map.setCheckable(False)
        self.pushBtn_Map.setObjectName("pushBtn_Map")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 540, 960, 190))
        self.groupBox_3.setObjectName("groupBox_3")
        self.iot_widget = QtWidgets.QWidget(self.groupBox_3)
        self.iot_widget.setGeometry(QtCore.QRect(5, 25, 800, 160))
        self.iot_widget.setObjectName("iot_widget")
        self.temp_label = QtWidgets.QLabel(self.groupBox_3)
        self.temp_label.setGeometry(QtCore.QRect(850, 36, 100, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.temp_label.setFont(font)
        self.temp_label.setObjectName("temp_label")
        self.humid_label = QtWidgets.QLabel(self.groupBox_3)
        self.humid_label.setGeometry(QtCore.QRect(850, 90, 100, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.humid_label.setFont(font)
        self.humid_label.setObjectName("humid_label")
        self.co_label = QtWidgets.QLabel(self.groupBox_3)
        self.co_label.setGeometry(QtCore.QRect(850, 150, 100, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.co_label.setFont(font)
        self.co_label.setObjectName("co_label")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_4.setGeometry(QtCore.QRect(970, 190, 301, 341))
        self.groupBox_4.setObjectName("groupBox_4")
        self.cB_Bell = QtWidgets.QCheckBox(self.groupBox_4)
        self.cB_Bell.setGeometry(QtCore.QRect(20, 40, 92, 23))
        self.cB_Bell.setObjectName("cB_Bell")
        self.cB_SMS = QtWidgets.QCheckBox(self.groupBox_4)
        self.cB_SMS.setGeometry(QtCore.QRect(20, 70, 92, 23))
        self.cB_SMS.setObjectName("cB_SMS")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 261, 211))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.videoPreview.setText(_translate("MainWindow", "Video Preview"))
        self.groupBox.setTitle(_translate("MainWindow", "IP Camera"))
        self.pushBtn_Video.setText(_translate("MainWindow", "Open Streams"))
        self.check_proc.setText(_translate("MainWindow", "Processing"))
        self.box_cam.setItemText(0, _translate("MainWindow", "001"))
        self.box_cam.setItemText(1, _translate("MainWindow", "002"))
        self.box_cam.setItemText(2, _translate("MainWindow", "003"))
        self.box_cam.setItemText(3, _translate("MainWindow", "004"))
        self.box_loc.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">192.168.1.xxx:554/Streaming/Channels/101/</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "General Settings"))
        self.pushBtn_Map.setText(_translate("MainWindow", "Display Map"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sensor Preview"))
        self.temp_label.setText(_translate("MainWindow", "T:"))
        self.humid_label.setText(_translate("MainWindow", "H:"))
        self.co_label.setText(_translate("MainWindow", "CO:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Notification"))
        self.cB_Bell.setText(_translate("MainWindow", "Bell"))
        self.cB_SMS.setText(_translate("MainWindow", "SMS"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Quach Cong Hoang"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "..."))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Phone number"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "+84936261441"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
