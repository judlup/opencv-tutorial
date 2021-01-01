# Read | Images - Videos - Webcam
import cv2
print("Package imported")


# Image

img = cv2.imread("Resources/tesla.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)


# Video

cap = cv2.VideoCapture("Resources/video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Webcam

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break