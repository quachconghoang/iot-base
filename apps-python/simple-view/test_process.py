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
    while (True):
        img0 = mng.camera_preview[0]
        img1 = mng.camera_preview[1]
        img2 = mng.camera_preview[2]
        img3 = mng.camera_preview[3]
        cv2.imshow('frame0', img0)
        cv2.imshow('frame1', img1)
        cv2.imshow('frame2', img2)
        cv2.imshow('frame3', img3)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    mng.callStoping()