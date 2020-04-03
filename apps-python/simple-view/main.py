import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QMainWindow,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt
from ui_mainwindow import Ui_MainWindow

from CameraManager import CameraManager

import cv2
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.magic)
        # self.ui.pushButton.clicked.connect(openCamera)

    @Slot()
    def magic(self):
        self.ui.pushButton.setText('abc');

def openCamera():
    cap = cv2.VideoCapture('rtsp://admin:1234Abc.@192.168.1.10:554/Streaming/Channels/101/')

    while (True):
        ret, frame = cap.read()
        frame_prev = cv2.resize(frame, dsize=(960,540))
        cv2.imshow('frame', frame_prev)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

config = '/home/hoangqc/IP_Camera.json'

if __name__ == "__main__":
    mng = CameraManager()
    mng.loadInfo(config)

    # app = QApplication(sys.argv)
    #
    # window = MainWindow()
    # window.show()
    #
    # sys.exit(app.exec_())