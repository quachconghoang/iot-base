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
        self.groupBox.setGeometry(QtCore.QRect(970, -1, 301, 541))
        self.groupBox.setObjectName("groupBox")
        self.pushBtn_Video = QtWidgets.QPushButton(self.groupBox)
        self.pushBtn_Video.setGeometry(QtCore.QRect(150, 490, 141, 40))
        self.pushBtn_Video.setCheckable(True)
        self.pushBtn_Video.setObjectName("pushBtn_Video")
        self.camIP_0 = QtWidgets.QLineEdit(self.groupBox)
        self.camIP_0.setGeometry(QtCore.QRect(90, 30, 201, 25))
        self.camIP_0.setObjectName("camIP_0")
        self.camIP_1 = QtWidgets.QLineEdit(self.groupBox)
        self.camIP_1.setGeometry(QtCore.QRect(90, 60, 201, 25))
        self.camIP_1.setObjectName("camIP_1")
        self.camIP_2 = QtWidgets.QLineEdit(self.groupBox)
        self.camIP_2.setGeometry(QtCore.QRect(90, 90, 201, 25))
        self.camIP_2.setObjectName("camIP_2")
        self.camIP_3 = QtWidgets.QLineEdit(self.groupBox)
        self.camIP_3.setGeometry(QtCore.QRect(90, 120, 201, 25))
        self.camIP_3.setObjectName("camIP_3")
        self.box_protocol_1 = QtWidgets.QComboBox(self.groupBox)
        self.box_protocol_1.setGeometry(QtCore.QRect(190, 180, 100, 25))
        self.box_protocol_1.setObjectName("box_protocol_1")
        self.box_protocol_1.addItem("")
        self.box_protocol_1.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(190, 210, 101, 23))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(190, 150, 100, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(970, 540, 301, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushBtn_Map = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBtn_Map.setGeometry(QtCore.QRect(150, 140, 141, 40))
        self.pushBtn_Map.setCheckable(True)
        self.pushBtn_Map.setObjectName("pushBtn_Map")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 540, 960, 190))
        self.groupBox_3.setObjectName("groupBox_3")
        self.iot_widget = QtWidgets.QWidget(self.groupBox_3)
        self.iot_widget.setGeometry(QtCore.QRect(0, 20, 960, 170))
        self.iot_widget.setObjectName("iot_widget")
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
        self.camIP_0.setText(_translate("MainWindow", "192.168.1.142"))
        self.camIP_1.setText(_translate("MainWindow", "192.168.1.142"))
        self.camIP_2.setText(_translate("MainWindow", "192.168.1.142"))
        self.camIP_3.setText(_translate("MainWindow", "192.168.1.142"))
        self.box_protocol_1.setItemText(0, _translate("MainWindow", "RTSP"))
        self.box_protocol_1.setItemText(1, _translate("MainWindow", "HTTPS"))
        self.checkBox.setText(_translate("MainWindow", "Processing"))
        self.lineEdit.setText(_translate("MainWindow", "554"))
        self.groupBox_2.setTitle(_translate("MainWindow", "General Settings"))
        self.pushBtn_Map.setText(_translate("MainWindow", "Display Map"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sensor Preview"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
