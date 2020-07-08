from SSDLib import SSDSmoke
import numpy as np
import threading
import cv2

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
        self.properties = []
        self.full_loc = []
        self.user_id = ''
        self.user_pwd = ''

    def path_at(self,i):
        return (self.protocol + self.user_id + ':' + self.user_pwd + '@' + self.locations[i])


class CameraManager():
    def __init__(self):
        self.SSDModel = SSDSmoke()
        self.cameraInfo = CameraInfo()
        self.camera_number = 0

        self.camera_thread = []
        self.camera_state = []

        self.camera_capture = []    #   cv2.Capture
        self.camera_preview = []    #   Mat

        self.camera_imgs = []       #   Raw Mat
        self.process_boxes = []   #   Processing Results
        self.process_scores = []
        self.drawResult = False

        self.size_raw_imgs = [IMG_w,    IMG_h]
        self.size_previews = [PRV_w,    PRV_h]


    def loadInfo(self, fname):
        fs = cv2.FileStorage(fname, cv2.FILE_STORAGE_READ)
        self.cameraInfo.protocol = fs.getNode('protocol').string()

        self.cameraInfo.user_id = fs.getNode('user-id').string()
        self.cameraInfo.user_pwd = fs.getNode('user-pwd').string()
        loc = fs.getNode('locations')
        prop = fs.getNode('properties')

        for i in range(loc.size()):
            self.cameraInfo.locations.append(loc.at(i).string())
            self.cameraInfo.properties.append(prop.at(i).real())
            if(self.cameraInfo.properties[i]==0):
                self.cameraInfo.full_loc.append(self.cameraInfo.path_at(i))
            else:
                self.cameraInfo.full_loc.append(loc.at(i).string())

            self.camera_state.append(CAMERA_STATUS.STOPPED)

            self.camera_preview.append(np.zeros((PRV_h, PRV_w, 3), dtype = "uint8"))
            self.camera_imgs.append(np.zeros((IMG_h, IMG_w, 3), dtype = "uint8"))

            self.camera_capture.append(cv2.VideoCapture())
            self.camera_thread.append(threading.Thread())
            print(self.cameraInfo.full_loc[i])

        self.camera_number = loc.size()
        print('Number of cam = ', self.camera_number)


    def drawOverLay(self, img, index):
        cv2.putText(img, str(index), (440, 40), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=3)
        if(self.drawResult):
            boxes = np.array(self.process_boxes[index])
            scores = np.array(self.process_scores[index])
            num_boxes = boxes.shape[0]
            scale = 480 / 1280
            for i in range(num_boxes):
                box = boxes[i]
                score = scores[i]

                color = (0, 255, 0)
                if score < 0.9 :
                    color = (0,255,255)
                    if score < 0.85:
                        color = (0,0,255)

                pt1 = ( int(box[0]*scale), int(box[1]*scale) )
                pt2 = ( int(box[2]*scale), int(box[3]*scale) )
                cv2.rectangle(img, pt1=pt1, pt2=pt2, color=color)


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
            self.camera_capture[i] = cv2.VideoCapture(self.cameraInfo.full_loc[i])
            self.camera_thread[i] = threading.Thread(target=self.stream_funtion, args=(i,))
            self.camera_thread[i].start()

    def callSSD(self):
        batch = []
        for index in range(self.camera_number):
            frame = cv2.cvtColor(self.camera_imgs[index], cv2.COLOR_BGR2RGB)
            batch.append(frame)
        # output = self.SSDModel.predict(batch)
        self.process_boxes, self.process_scores = self.SSDModel.predict_boxes(batch)

        # for index in range(self.camera_number):
        #     frame = cv2.cvtColor(output[index], cv2.COLOR_RGB2BGR)
        #     self.camera_preview[index] = cv2.resize(frame, dsize=(PRV_w, PRV_h))
            # self.drawOverLay( self.camera_preview[index],index)
        return

    def callStoping(self):
        for i in range(self.camera_number):
            self.camera_state[i] = CAMERA_STATUS.STOPPING
            if self.camera_thread[i].is_alive():
                self.camera_thread[i].join()

