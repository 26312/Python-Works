import cv2
import numpy as np

cap = cv2.VideoCapture(0)
bg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = bg.apply(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('bg',fgmask)


    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()