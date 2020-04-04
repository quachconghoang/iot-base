import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QMainWindow,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.magic)
        # self.ui.pushButton.clicked.connect(openCamera)
        # self.mng = CameraManager()
        # self.mng.loadInfo(config)

    @Slot()
    def magic(self):
        self.ui.pushButton.setText('abc');



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())