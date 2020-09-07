import numpy as np
import cv2

path4 = "/home/hoangqc/Desktop/006.mp4"
raw_size = (1280, 720)
proc_size = (640, 360)

p0 = (250, 0)
roi_size = (360, 360)
p1 = (p0[0]+roi_size[0],p0[1]+roi_size[1])

proc_roi = (p0[0], p0[1], roi_size[0], roi_size[1])

flow_points_thresh = 1000

dl_size = (300,300)



cap = cv2.VideoCapture(path4)
count = 0

ret, dumb = cap.read()
frame = cv2.resize(dumb, proc_size)
# prvs = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
prvs = np.zeros(roi_size,dtype=np.uint8)

hsv = np.zeros_like(frame)
hsv[...,1] = 255


while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
    ret = cap.grab()
    if (ret):

        if(count%15 == 0):
            cap.read(dumb)
            # cv2.imwrite('/home/hoangqc/Desktop/Frames-05/frame'+str(count)+'.jpg',dumb)
            frame = cv2.resize(dumb, proc_size)
            roi_img = frame[p0[1]:p1[1], p0[0]:p1[0]]
            next = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            flow_func = 0.8*abs(flow[..., 1]) + 0.2*abs(flow[..., 0])
            # minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(flow_func)
            # print(maxVal, maxLoc)

            ret1, flow_mask = cv2.threshold(flow_func, 0.8, 1, cv2.THRESH_BINARY)

            points = np.nonzero(flow_mask)
            point_org = (p1[0]/2, p1[1]/2)

            num_point = points[0].size


            if num_point == 0:
                pass
            else:
                point_org = (np.mean(points[1]).astype(int),
                             np.mean(points[0]).astype(int))
            print(point_org)

            cv2.imshow('flow_mask', flow_mask)
            # cv2.imshow('flow_x', flow_x)
            # cv2.imshow('flow_y', flow_y)

            if num_point>flow_points_thresh:
                # cv2.circle(roi_img, maxLoc, 7, (255,255,0), 2)
                print(num_point)
                cv2.circle(roi_img, point_org, 7, (0,0,255), 2)

            cv2.rectangle(frame, p0, p1, (0,0,255), 1)

            cv2.imshow('frame', frame)
            # cv2.imshow('roi',roi_img)

            prvs = next
            # cv2.waitKey()

        count += 1

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()