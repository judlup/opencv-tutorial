# Warp Prespective

import cv2
import numpy as np

img = cv2.imread("Resources/tesla.jpg")

width,height = 250,350
pts = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput )

cv2.waitKey(0)