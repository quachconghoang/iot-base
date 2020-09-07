import numpy as np
import cv2
from SSDLib import SSDSmoke

path4 = "/home/hoangqc/Desktop/005.mp4"
raw_size = (1280, 720)
proc_size = (640, 360)

p0 = (140, 0)
roi_size = (360, 360)
p1 = (p0[0]+roi_size[0],p0[1]+roi_size[1])
proc_roi = (p0[0], p0[1], roi_size[0], roi_size[1])
flow_points_thresh = 500

dl_size = (300,300)
dl_radius = 150


cap = cv2.VideoCapture(path4)
count = 0

ret, dumb = cap.read()
frame = cv2.resize(dumb, proc_size)
# prvs = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
prvs = np.zeros(roi_size,dtype=np.uint8)

SSDModel = SSDSmoke()
SSDModel.preparingModel()
process_boxes = []  # Processing Results
process_scores = []

def getROI_DL(_proc_size = (640,360), dl_radius = 150, _org =  (240,180)):
    Ox = (_org[0])
    Oy = (_org[1])
    if Ox < dl_radius: Ox = dl_radius
    if Ox > (_proc_size[0] - dl_radius):    Ox = (_proc_size[0] - dl_radius)
    if Oy < dl_radius: Oy = dl_radius
    if Oy > (_proc_size[1] - dl_radius):    Oy = (_proc_size[1] - dl_radius)

    p0 = (Ox-dl_radius, Oy-dl_radius)
    p1 = (Ox+dl_radius, Oy+dl_radius)

    return p0,p1

# dl_p0, dl_p1 = getROI_DL(_proc_size=proc_size, dl_radius=180)

while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
    ret = cap.grab()
    if (ret):

        if(count%30 == 0):
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
            point_org = (int(p1[0]/2), int(p1[1]/2))

            num_point = points[0].size
            cv2.imshow('flow_mask', flow_mask)

            if num_point>flow_points_thresh:
                print(num_point)
                point_org = (np.mean(points[1]).astype(int) + p0[0],
                             np.mean(points[0]).astype(int) + p0[1])
                # cv2.circle(frame, point_org, 7, (0,0,255), 2)
                dl_p0, dl_p1 = getROI_DL(_proc_size=proc_size, dl_radius=dl_radius, _org=point_org)

            else:
                dl_p0 = p0
                dl_p1 = p1

            dl_mat = frame[dl_p0[1]:dl_p1[1], dl_p0[0]:dl_p1[0]]
            # print(dl_p0, dl_p1)

            batch = []
            dl_matx = cv2.cvtColor(dl_mat, cv2.COLOR_BGR2RGB)
            batch.append(dl_matx)
            process_boxes, process_scores = SSDModel.predict_boxes(batch)

            boxes = np.array(process_boxes[0])
            scores = np.array(process_scores[0])
            num_boxes = boxes.shape[0]
            for i in range(num_boxes):
                box = boxes[i]
                score = scores[i]

                if score < 0.9 :
                    color = (0,255,255)
                    if score < 0.85:
                        color = (0,0,255)
                else:
                    color = (0, 255, 0)
                    print('hit')

                rsp1 = ( int(box[0] + dl_p0[0]), int(box[1] + dl_p0[1]) )
                rsp2 = ( int(box[2] + dl_p0[0]), int(box[3] + dl_p0[1]) )
                cv2.rectangle(frame, pt1=rsp1, pt2=rsp2, color=color)


            cv2.rectangle(frame, dl_p0, dl_p1, (0, 255, 255), 2)
            # cv2.rectangle(frame, p0, p1, (0,0,255), 1)
            cv2.imshow('frame', frame)
            # cv2.imshow('x', dl_mat)
            # cv2.imshow('roi',roi_img)

            prvs = next
            # cv2.waitKey()

        count += 1

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()