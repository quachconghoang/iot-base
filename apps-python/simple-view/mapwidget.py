from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2 import QtCore

class MapWidget(QWidget):
    def __init__(self, parent=None):
        super(MapWidget, self).__init__(parent)
        self.resize(1280,720)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)  # <---

        self.setWindowTitle('Sơ đồ tòa nhà')

        button_close = QPushButton(self)
        button_close.setText('Close')
        button_close.setGeometry(QtCore.QRect(1070, 670, 200, 40))
        button_close.clicked.connect(self.hide)


        # grid = QGridLayout(self)
        # grid.addWidget(button)

