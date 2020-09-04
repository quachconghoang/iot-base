import numpy as np
import cv2

path4 = "/home/hoangqc/Desktop/005.mp4"

cap = cv2.VideoCapture(path4)
count = 0

ret, dumb = cap.read()
frame = cv2.resize(dumb, dsize=(640, 360))
prvs = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


hsv = np.zeros_like(frame)
hsv[...,1] = 255


while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
    ret = cap.grab()
    if (ret):

        if(count%15 == 0):
            cap.read(dumb)
            cv2.imwrite('/home/hoangqc/Desktop/Frames-05/frame'+str(count)+'.jpg',dumb)
            frame = cv2.resize(dumb, dsize=(640, 360))
            cv2.imshow('frame', frame)
            next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            hsv[..., 0] = ang * 180 / np.pi / 2
            hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            cv2.imshow('frame2', rgb)

            prvs = next

        count += 1
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    # cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()