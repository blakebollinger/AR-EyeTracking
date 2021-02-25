import cv2 as cv
import numpy as np
import glob

# cap = cv.VideoCapture('../data/20201107_012909_HoloLens.mp4')
cap = cv.VideoCapture('../data/001/world.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    color = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    cv.imshow('frame', color)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv.destroyAllWindows()