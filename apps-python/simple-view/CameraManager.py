import cv2
import numpy as np
import threading

import time
from enum import Enum

from config import *

class CAMERA_STATUS(Enum):
    STOPPED = 0
    STARTED = 1
    STOPPING = 2

class CameraInfo():
    def __init__(self):
        self.protocol = 'rtsp://'
        self.locations = []
        self.user_id = ''
        self.user_pwd = ''

    def path_at(self,i):
        return (self.protocol + self.user_id + ':' + self.user_pwd + '@' + self.locations[i])


class CameraManager():
    def __init__(self):
        self.cameraInfo = CameraInfo()
        self.camera_number = 0

        self.camera_thread = []
        self.camera_state = []

        self.camera_capture = []    #   cv2.Capture
        self.camera_preview = []    #   Mat

        self.camera_imgs = []       #   Raw Mat
        self.process_results = []   #   Processing Results

        self.size_raw_imgs = [IMG_w,    IMG_h]
        self.size_previews = [PRV_w,    PRV_h]


    def loadInfo(self, fname):
        fs = cv2.FileStorage(fname, cv2.FILE_STORAGE_READ)
        self.cameraInfo.protocol = fs.getNode('protocol').string()

        self.cameraInfo.user_id = fs.getNode('user-id').string()
        self.cameraInfo.user_pwd = fs.getNode('user-pwd').string()
        loc = fs.getNode('locations')
        self.camera_number = loc.size()
        print('Number of cam = ', self.camera_number)

        for i in range(self.camera_number):
            self.cameraInfo.locations.append(loc.at(i).string())
            self.camera_state.append(CAMERA_STATUS.STOPPED)

            self.camera_preview.append(np.zeros((PRV_h, PRV_w, 3), dtype = "uint8"))
            self.camera_imgs.append(np.zeros((IMG_h, IMG_w, 3), dtype = "uint8"))

            self.camera_capture.append(cv2.VideoCapture())
            self.camera_thread.append(threading.Thread())
            print(self.cameraInfo.path_at(i))

    def drawOverLay(self, img, index):
        img= cv2.putText(img, str(index), (10, 40), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                                    fontScale=1, color=(0, 0, 255), thickness=3)

    def stream_funtion(self, index):
        cap = self.camera_capture[index]
        self.camera_state[index] = CAMERA_STATUS.STARTED
        while (self.camera_state[index] != CAMERA_STATUS.STOPPING):
            ret, self.camera_imgs[index] = cap.read()
            if(ret):
                self.camera_preview[index] = cv2.resize(self.camera_imgs[index], dsize=(PRV_w, PRV_h))

                self.drawOverLay( self.camera_preview[index],index)

                # cv2.imshow('frame'+str(index), self.camera_preview[index])
                # cv2.waitKey(0)
                time.sleep(CAM_interval)
        self.camera_state[index] = CAMERA_STATUS.STOPPED
        cap.release()
        print('Thread ', index, ' ended ---')

    def openStreams(self):
        for i in range(self.camera_number):
            print('Opening stream number',i)
            self.camera_capture[i] = cv2.VideoCapture(self.cameraInfo.path_at(i))
            self.camera_thread[i] = threading.Thread(target=self.stream_funtion, args=(i,))
            self.camera_thread[i].start()

    def callStoping(self):
        for i in range(self.camera_number):
            self.camera_state[i] = CAMERA_STATUS.STOPPING
            self.camera_thread[i].join()

