import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

prvs = cv2.imread("/home/hoangqc/Desktop/Frames-05/frame1140.jpg")
prvs = cv2.cvtColor(prvs, cv2.COLOR_BGR2GRAY)
next = cv2.imread("/home/hoangqc/Desktop/Frames-05/frame1155.jpg")
next = cv2.cvtColor(next, cv2.COLOR_BGR2GRAY)
flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

plt.imshow(flow)
plt.show()