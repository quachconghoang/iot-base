import cv2
import numpy as np
import threading

from enum import Enum
class CAMERA_STATUS(Enum):
    EMPTY = 0
    STARTED = 1
    STOPPED = 2

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
        self.camera_number = 0

    def loadInfo(self, fname):
        fs = cv2.FileStorage(fname, cv2.FILE_STORAGE_READ)
        self.cameraInfo.protocol = fs.getNode('protocol').string()

        self.cameraInfo.user_id = fs.getNode('user-id').string()
        self.cameraInfo.user_pwd = fs.getNode('user-pwd').string()

        loc = fs.getNode('locations')
        self.camera_number = loc.size()
        for i in range(self.camera_number):
            self.cameraInfo.locations.append(loc.at(i).string())
            print(self.cameraInfo.path_at(i))
            self.camera_state.append(CAMERA_STATUS.EMPTY)

    def openStreams(self):
        for i in range(self.camera_number):
            cap = cv2.VideoCapture(self.cameraInfo.path_at(i))
            self.camera_capture.append(cap)

    def gettingVideos(self):
        cap = self.camera_capture[0]
        while (True):
            ret, frame = cap.read()
            frame_prev = cv2.resize(frame, dsize=(960, 540))
            cv2.imshow('frame', frame_prev)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break