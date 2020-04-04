import cv2
import numpy as np
import threading

import time
from enum import Enum

PRV_w = 640
PRV_h = 360
CAM_interval =  0.015

class CAMERA_STATUS(Enum):
    EMPTY = 0
    STARTED = 1
    STOPPING = 2
    STOPPED = 3

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
        self.camera_thread = []
        self.camera_state = []
        self.camera_capture = []
        self.camera_preview = []
        self.camera_number = 0

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
            self.camera_state.append(CAMERA_STATUS.EMPTY)
            self.camera_preview.append(np.zeros((PRV_h, PRV_w, 4), dtype = "uint8"))
            print(self.cameraInfo.path_at(i))

    def stream_funtion(self, index):
        cap = self.camera_capture[index]
        self.camera_state[index] = CAMERA_STATUS.STARTED
        while (self.camera_state[index] != CAMERA_STATUS.STOPPING):
            ret, frame = cap.read()
            if(ret):
                self.camera_preview[index] = cv2.resize(frame, dsize=(PRV_w, PRV_h))
                time.sleep(CAM_interval)
        self.camera_state[index] = CAMERA_STATUS.STOPPED
        # print(index, ' ended')

    def openStreams(self):
        for i in range(self.camera_number):
            print('Opening stream number',i)
            cap = cv2.VideoCapture(self.cameraInfo.path_at(i))
            self.camera_capture.append(cap)
            cap_thread = threading.Thread(target=self.stream_funtion, args=(i,))
            cap_thread.start()
            self.camera_thread.append(cap_thread)

    def callStoping(self):
        for i in range(self.camera_number):
            self.camera_state[i] = CAMERA_STATUS.STOPPING