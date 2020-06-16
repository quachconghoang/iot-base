import sys
import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QMainWindow, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

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
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(1280,800)

        self.mng = CameraManager()
        self.mng.loadInfo('./IP_Camera.json')

        self.setupGUI_Video()
        self.setupGUI_Iots()

        self.map_view = MapWidget(self)
        self.ui.pushBtn_Video.clicked.connect(self.openCamera)
        self.ui.pushBtn_Map.clicked.connect(self.map_view.show)

    def setupGUI_Video(self):
        self.img_dumb = np.zeros((540, 960, 3), dtype="uint8")
        self.img_dumb.fill(128)
        self.img_preview = np.zeros((540, 960, 3), dtype="uint8")
        self.ui.videoPreview.setPixmap(QPixmap.fromImage(QImage(self.img_dumb,  PRV_w * 2, PRV_h * 2, QImage.Format_RGB888)))
        self.timer_videos = QTimer(self)
        self.timer_videos.timeout.connect(self.updateVideos)
        self.timer_videos.setInterval(30)

        # self.ui.box_cam.currentIndexChanged.connect(self.camera_Changed)
        # self.ui.box_cam.activated.connect(self.camera_Saved)
        # self.camera_Changed()

        self.timer_proc = QTimer(self)
        self.timer_proc.timeout.connect(self.img_processing)
        self.timer_proc.setInterval(1000)
        self.timer_proc.start()

        self.ui.check_proc.setEnabled(False)

        # self.ui.check_proc.clicked.connect(self.processStatusChanged)
        self.ui.cB_Bell.clicked.connect(self.notifcationStatusChanged)
        self.ui.cB_SMS.clicked.connect(self.notifcationStatusChanged)
        # self.mng.cameraInfo.locations.

    def setupGUI_Iots(self):
        self.mqttc = mqtt.Client()
        self.mqttc.on_message = self.on_iot_message
        self.mqttc.connect("127.0.0.1", 1883, 60)
        self.mqttc.subscribe("demo/test", qos=0)
        self.mqttc.loop_start()

        self.iot_canvas = MplCanvas(self.ui.iot_widget, width=8.0, height=1.6, dpi=100)
        self.ui.temp_label.setStyleSheet("color: red")
        self.ui.humid_label.setStyleSheet("color: blue")

    @Slot()
    def openCamera(self):
        if(self.ui.pushBtn_Video.text() == 'Open Streams'):
            self.mng.openStreams()
            self.timer_videos.start()
            self.ui.check_proc.setEnabled(True)
            self.ui.pushBtn_Video.setText('CLOSE')
        else:
            self.timer_videos.stop()
            self.ui.check_proc.setChecked(False)
            self.ui.check_proc.setEnabled(False)

            self.mng.callStoping()
            self.ui.pushBtn_Video.setText('Open Streams')
            self.ui.videoPreview.setPixmap(QPixmap.fromImage(QImage(self.img_dumb,
                                         PRV_w * 2, PRV_h * 2, QImage.Format_RGB888)))

    @Slot()
    def img_processing(self):
        if(self.ui.check_proc.isChecked()):
            if(self.mng.SSDModel.isReady == False): self.mng.SSDModel.preparingModel()

                # self.mng.drawResult = False
            self.mng.callSSD()
            self.mng.drawResult = True
        else:
            self.mng.drawResult = False

    @Slot()
    def processStatusChanged(self):
        print("..." + str(self.ui.check_proc.checkState()))

    @Slot()
    def notifcationStatusChanged(self):

        print("...")


    @Slot()
    def updateVideos(self):
        # self.mng.callSSD()
        self.img_preview[0:PRV_h, 0:PRV_w] = self.mng.camera_preview[0]
        if(self.mng.camera_number>1):
            self.img_preview[0:PRV_h, PRV_w:(PRV_w * 2)] = self.mng.camera_preview[1]
        if (self.mng.camera_number > 2):
            self.img_preview[PRV_h:PRV_h * 2, 0:PRV_w] = self.mng.camera_preview[2]
        if (self.mng.camera_number > 3):
            self.img_preview[PRV_h:PRV_h * 2, PRV_w:PRV_w * 2] = self.mng.camera_preview[3]

        self.ui.videoPreview.setPixmap(
            QPixmap.fromImage(QImage(self.img_preview, PRV_w * 2, PRV_h * 2, QImage.Format_RGB888).rgbSwapped()))

    def on_iot_message(self, mqttc, obj, msg):
        print('Update IoTs ...')
        payload = json.loads(msg.payload)  # you can use json.loads to convert string to json
        self.ui.temp_label.setText("T: " + str(payload['t']) + " ℃")
        self.ui.humid_label.setText("H: " + str(payload['h']) + " %")
        self.ui.co_label.setText("CO: " + str(payload['MQ7']) + " ppm")
        # print(payload['t'], payload['h'], payload['MQ7'])  # then you can check the value
        self.iot_canvas.updateData(json.loads(msg.payload))

    def alarming_message(self):
        exit()

    def closeEvent(self, event:PyQt5.QtGui.QCloseEvent):
        print('App is closing ...')
        self.mng.callStoping()