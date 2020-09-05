import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

prvs = cv2.imread("/home/hoangqc/Desktop/Frames-05/frame1140.jpg")
prvs = cv2.cvtColor(prvs, cv2.COLOR_BGR2GRAY)
next = cv2.imread("/home/hoangqc/Desktop/Frames-05/frame1155.jpg")
next = cv2.cvtColor(next, cv2.COLOR_BGR2GRAY)
flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

flow_x = flow[..., 0]
flow_y = flow[..., 1]
ret1, th_x = cv2.threshold(flow_x, 0.8, 1, cv2.THRESH_BINARY)
cv2.imshow('th_x', th_x)

cv2.imshow('flow_x', flow_x)
cv2.imshow('flow_y', flow_y)
cv2.waitKey()