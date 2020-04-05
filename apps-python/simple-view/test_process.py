import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QMainWindow,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt
from ui_mainwindow import Ui_MainWindow

from CameraManager import CameraManager

import cv2
import numpy as np

config = './IP_Camera.json'

if __name__ == '__main__':
    mng = CameraManager()
    mng.loadInfo(config)
    mng.openStreams()
    fullView = np.zeros((540, 960, 3), dtype="uint8")
    while (True):
        fullView[0:270, 0:480] = mng.camera_preview[0].copy()
        fullView[0:270, 480:960] = mng.camera_preview[1].copy()
        fullView[270:540, 0:480] = mng.camera_preview[2].copy()
        fullView[270:540, 480:960] = mng.camera_preview[3].copy()
        cv2.imshow('frame0', fullView)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    mng.callStoping()