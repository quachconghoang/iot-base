from SSDLib import SSDSmoke
import numpy as np 
import glob
import os
import cv2
import time
from PIL import Image

tmp = SSDSmoke()

vcap = cv2.VideoCapture("rtsp://admin:1234Abc.@10.10.0.166:554/Streaming/Channels/101/")
while(1):
    batch = []
    ret, frame = vcap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    batch.append(frame)
    output = tmp.predict(batch)
    cv2.imshow('VIDEO', output[0])
    # pil_img = Image.fromarray(frame)
    # pil_img.save('lena_bgr_pillow.jpg')
    # print(type(frame), frame.shape)
    key = cv2.waitKey(1) 
    if key == 113: # 'q'
        break
        

'''
tmp = SSDSmoke()

batch = []
image_paths = glob.glob(os.path.join("/home/thangnv/Github/SSD/demo/", '*.png'))

for i, image_path in enumerate(image_paths):
    image_name = os.path.basename(image_path)
    image = np.array(Image.open(image_path).convert("RGB"))
    batch.append(image)
    
out = tmp.predict(batch)
print(len(out))
'''