import sys
import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QMainWindow, QGraphicsView,
                               QVBoxLayout, QWidget, QGraphicsPixmapItem)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from ui_mainwindow import Ui_MainWindow
from CameraManager import CameraManager
from mapwidget import MapWidget
import time

import numpy as np
# import cv2
from config import *


# class Canvas(FigureCanvas):
#     def __init__(self, parent=None, width=5, height=5, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#         self.plot()
#
#     def plot(self):
#         x = np.array([50, 30, 40])
#         labels = ["Apples", "Bananas", "Melons"]
#         ax = self.figure.add_subplot(111)
#         ax.pie(x, labels=labels)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Ứng dụng Quản lý Camera Cảnh báo cháy')

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
        self.timer_iots = QTimer(self)
        self.timer_iots.timeout.connect(self.updateIoTs)
        self.timer_iots.setInterval(1000)
        self.timer_iots.start()

        self.map_view = MapWidget(self)
        self.ui.pushButton.clicked.connect(self.openCamera)
        self.ui.pushBtn_Map.clicked.connect(self.map_view.show)


    # def MyUI(self):
    #     canvas = Canvas(self, width=8, height=4)
    #     canvas.move(10, 10)


    @Slot()
    def openCamera(self):
        if(self.ui.pushButton.text() == 'Open Streams'):
            self.mng.openStreams()
            self.timer_videos.start()
            self.ui.pushButton.setText('CLOSE')
        else:
            self.timer_videos.stop()
            self.mng.callStoping()
            self.ui.pushButton.setText('Open Streams')
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

    @Slot()
    def updateIoTs(self):
        print('Update IoTs ...')

    def closeEvent(self, event:PyQt5.QtGui.QCloseEvent):
        print('App is closing ...')
        self.mng.callStoping()

#   https://stackoverflow.com/questions/58075822/pyside2-and-matplotlib-how-to-make-matplotlib-run-in-a-separate-process-as-i