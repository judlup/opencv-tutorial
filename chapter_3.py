# Resizing and cropping

import cv2
import numpy as np

img = cv2.imread("Resources/tesla.jpg")

print(img.shape)

imgResize = cv2.resize(img,(522,486))

imgCropped = img[0:200,20:200]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
