import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    _,frame  = cap.read();
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(frame,(5,5),0)

    canny = cv2.Canny(blurred_frame,30,30)
    # sobelx = cv2.Sobel(blurred_frame,cv2.CV_64F,1,0,ksize=5)
    # sobely = cv2.Sobel(blurred_frame, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imshow('Frame',frame)
    cv2.imshow('Canny',canny)
    # cv2.imshow('SobelX',sobelx)
    # cv2.imshow('SobelY', sobely)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

