from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

from config import *
from ui_mapwidget import Ui_MapWidget

class MapWidget(QWidget):
    def __init__(self, parent=None):
        super(MapWidget, self).__init__()
        self.ui = Ui_MapWidget()
        self.ui.setupUi(self)

        self.setWindowTitle(k_Title_AppMap)
        self.ui.closeButton.clicked.connect(self.hide)

        self.maps = ('./Resources/01.png','./Resources/02.png','./Resources/03.png',
                     './Resources/04.png','./Resources/05.png','./Resources/06.png',
                     './Resources/07.png')
        self.currentMap = QPixmap(self.maps[0])

        self.ui.imageLB.setPixmap(self.currentMap)
        self.ui.layerSlider.setMaximum(len(self.maps)-1)
        self.ui.layerSlider.valueChanged.connect(self.changeMap)

    # def show(self):
    #     super(MapWidget, self).show()
    #     pass

    @Slot()
    def changeMap(self):
        mapID = self.ui.layerSlider.value()
        self.currentMap = QPixmap(self.maps[mapID])
        self.ui.imageLB.setPixmap(self.currentMap)
