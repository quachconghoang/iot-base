import sys
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QMainWindow, QGraphicsView,
                               QVBoxLayout, QWidget, QGraphicsPixmapItem)
from PySide2.QtCore import Slot, Qt, QTimer
from PySide2.QtGui import *
from ui_mainwindow import Ui_MainWindow
from CameraManager import CameraManager
import threading,time

import numpy as np
# import cv2
from config import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.mng = CameraManager()
        self.mng.loadInfo('./IP_Camera.json')

        self.ui.pushButton.clicked.connect(self.openCamera)

        self.img_dumb = np.zeros((540, 960, 3), dtype="uint8")
        self.img_dumb.fill(128)

        self.img_preview = np.zeros((540, 960, 3), dtype="uint8")

        self.ui.videoPreview.setPixmap(QPixmap.fromImage(QImage(self.img_dumb,  PRV_w * 2, PRV_h * 2, QImage.Format_BGR888)))
        self.thread_video = threading.Thread()

        self.need_update_videos = False
        self.need_update_iots = False

    @Slot()
    def openCamera(self):
        if(self.ui.pushButton.text() == 'Open Streams'):
            self.mng.openStreams()
            self.ui.pushButton.setText('CLOSE')
            self.need_update_videos = True
            self.thread_video = threading.Thread(target=self.updateVideos)
            self.thread_video.start()
        else:
            self.need_update_videos = False
            self.mng.callStoping()
            self.ui.pushButton.setText('Open Streams')
            self.thread_video.join()


    def updateVideos(self):
        while(self.need_update_videos):

            self.img_preview[0:PRV_h, 0:PRV_w] = self.mng.camera_preview[0]
            self.img_preview[0:PRV_h, PRV_w:(PRV_w * 2)] = self.mng.camera_preview[1]
            self.img_preview[PRV_h:PRV_h * 2, 0:PRV_w] = self.mng.camera_preview[2]
            self.img_preview[PRV_h:PRV_h * 2, PRV_w:PRV_w * 2] = self.mng.camera_preview[3]

            self.ui.videoPreview.setPixmap(QPixmap.fromImage(QImage(self.img_preview, PRV_w*2, PRV_h*2, QImage.Format_BGR888)))
            time.sleep(0.033)

        self.ui.videoPreview.setPixmap(QPixmap.fromImage(QImage(self.img_dumb, PRV_w * 2, PRV_h * 2, QImage.Format_BGR888)))

    # def updateVideos(self):
    #     print('Update Video')

    def updateIoTs(self):
        while(True):
            print('Update IoTs')
            time.sleep(1.0)


#   https://stackoverflow.com/questions/58075822/pyside2-and-matplotlib-how-to-make-matplotlib-run-in-a-separate-process-as-i