# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MapWidget(object):
    def setupUi(self, MapWidget):
        MapWidget.setObjectName("MapWidget")
        MapWidget.resize(1120, 840)
        self.imageLB = QtWidgets.QLabel(MapWidget)
        self.imageLB.setGeometry(QtCore.QRect(10, 10, 1024, 768))
        self.imageLB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageLB.setScaledContents(False)
        self.imageLB.setObjectName("imageLB")
        self.layerSlider = QtWidgets.QSlider(MapWidget)
        self.layerSlider.setGeometry(QtCore.QRect(1070, 10, 30, 768))
        self.layerSlider.setMaximum(10)
        self.layerSlider.setPageStep(1)
        self.layerSlider.setOrientation(QtCore.Qt.Vertical)
        self.layerSlider.setInvertedAppearance(False)
        self.layerSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.layerSlider.setObjectName("layerSlider")
        self.closeButton = QtWidgets.QPushButton(MapWidget)
        self.closeButton.setGeometry(QtCore.QRect(10, 790, 1100, 40))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(MapWidget)
        QtCore.QMetaObject.connectSlotsByName(MapWidget)

    def retranslateUi(self, MapWidget):
        _translate = QtCore.QCoreApplication.translate
        MapWidget.setWindowTitle(_translate("MapWidget", "Form"))
        self.imageLB.setText(_translate("MapWidget", "TextLabel"))
        self.closeButton.setText(_translate("MapWidget", "Close"))
