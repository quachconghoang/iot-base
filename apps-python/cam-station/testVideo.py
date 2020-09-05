import numpy as np
import cv2

path4 = "/home/hoangqc/Desktop/006.mp4"
raw_size = (1280, 720)
proc_size = (640, 360)
proc_roi = (140, 0, 360, 360)

cap = cv2.VideoCapture(path4)
count = 0

ret, dumb = cap.read()
frame = cv2.resize(dumb, proc_size)
prvs = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


hsv = np.zeros_like(frame)
hsv[...,1] = 255


while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
    ret = cap.grab()
    if (ret):

        if(count%5 == 0):
            cap.read(dumb)
            # cv2.imwrite('/home/hoangqc/Desktop/Frames-05/frame'+str(count)+'.jpg',dumb)
            frame = cv2.resize(dumb, proc_size)
            next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            flow_func = 0.8*abs(flow[..., 1]) + 0.2*abs(flow[..., 0])
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(flow_func)
            # print(maxVal, maxLoc)

            ret1, flow_mask = cv2.threshold(flow_func, 0.8, 1, cv2.THRESH_BINARY)
            points = np.nonzero(flow_mask)
            point_org = (proc_size[0]/2,proc_size[1]/2)

            num_point = points[0].size
            print(num_point)

            if num_point == 0:
                point_org = (10,10)
            else:
                point_org = (np.mean(points[1]).astype(int),
                             np.mean(points[0]).astype(int))
            print(point_org)

            # cv2.imshow('flow_mask', flow_mask)
            # cv2.imshow('flow_x', flow_x)
            # cv2.imshow('flow_y', flow_y)

            if num_point>150:
                cv2.circle(frame, maxLoc, 7, (255,255,0), 2)
                cv2.circle(frame, point_org, 7, (0,0,255), 2)

            cv2.rectangle(frame, (140,0), (140+360,360), (0,0,255), 1)

            cv2.imshow('frame', frame)

            prvs = next
            # cv2.waitKey()


        count += 1
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    # cv2.imshow('frame',frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()