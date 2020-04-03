import cv2
import numpy as np
import struct

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

    def loadInfo(self, fname):
        fs = cv2.FileStorage(fname, cv2.FILE_STORAGE_READ)
        self.cameraInfo.protocol = fs.getNode('protocol').string()

        self.cameraInfo.user_id = fs.getNode('user-id').string()
        self.cameraInfo.user_pwd = fs.getNode('user-pwd').string()

        loc = fs.getNode('locations')
        for i in range(loc.size()):
            self.cameraInfo.locations.append(loc.at(i).string())
            print(self.cameraInfo.path_at(i))


