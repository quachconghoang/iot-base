import sys
import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QMainWindow, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

import random

from ui_mainwindow import Ui_MainWindow
from CameraManager import CameraManager
from mapwidget import MapWidget

import paho.mqtt.client as mqtt
from mplcanvas import MplCanvas
import json

import numpy as np
from config import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(k_Title_App)

        self.mng = CameraManager()
        self.mng.loadInfo('./IP_Camera.json')

        self.img_dumb = np.zeros((540, 960, 3), dtype="uint8")
        self.img_dumb.fill(128)

        self.img_preview = np.zeros((540, 960, 3), dtype="uint8")

        self.ui.videoPreview.setPixmap(QPixmap.fromImage(QImage(self.img_dumb,  PRV_w * 2, PRV_h * 2, QImage.Format_RGB888)))

        self.timer_videos = QTimer(self)
        self.timer_videos.timeout.connect(self.updateVideos)
        self.timer_videos.setInterval(30)

        # self.MyUI()
        self.mqttc = mqtt.Client()
        self.mqttc.on_message = self.on_iot_message
        self.mqttc.connect("127.0.0.1", 1883, 60)
        self.mqttc.subscribe("test", qos=0)
        self.mqttc.loop_start()

        self.iot_canvas = MplCanvas(self.ui.iot_widget, width=9.6, height=1.7, dpi=100)

        self.map_view = MapWidget(self)
        self.ui.pushBtn_Video.clicked.connect(self.openCamera)
        self.ui.pushBtn_Map.clicked.connect(self.map_view.show)

    @Slot()
    def openCamera(self):
        if(self.ui.pushBtn_Video.text() == 'Open Streams'):
            self.mng.openStreams()
            self.timer_videos.start()
            self.ui.pushBtn_Video.setText('CLOSE')
        else:
            self.timer_videos.stop()
            self.mng.callStoping()
            self.ui.pushBtn_Video.setText('Open Streams')
            self.ui.videoPreview.setPixmap(QPixmap.fromImage(QImage(self.img_dumb,
                                         PRV_w * 2, PRV_h * 2, QImage.Format_RGB888)))

    @Slot()
    def updateVideos(self):
        self.img_preview[0:PRV_h, 0:PRV_w] = self.mng.camera_preview[0]
        self.img_preview[0:PRV_h, PRV_w:(PRV_w * 2)] = self.mng.camera_preview[1]
        self.img_preview[PRV_h:PRV_h * 2, 0:PRV_w] = self.mng.camera_preview[2]
        self.img_preview[PRV_h:PRV_h * 2, PRV_w:PRV_w * 2] = self.mng.camera_preview[3]

        self.ui.videoPreview.setPixmap(
            QPixmap.fromImage(QImage(self.img_preview, PRV_w * 2, PRV_h * 2, QImage.Format_RGB888).rgbSwapped()))

    # @Slot()
    # def updateIoTs(self):
    #     print('Update IoTs ...')

    def on_iot_message(self, mqttc, obj, msg):
        print('Update IoTs ...')
        payload = json.loads(msg.payload)  # you can use json.loads to convert string to json
        print(payload['t'])  # then you can check the value
        self.iot_canvas.updateData(json.loads(msg.payload))

    def closeEvent(self, event:PyQt5.QtGui.QCloseEvent):
        print('App is closing ...')
        self.mng.callStoping()

#   https://stackoverflow.com/questions/58075822/pyside2-and-matplotlib-how-to-make-matplotlib-run-in-a-separate-process-as-i