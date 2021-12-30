import os
import time
import HandTrackingModule as htm
import numpy as np
import cv2


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.85)

while True:
    success, img = cap.read()

    #find the hands
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=True)

    #tip of the index and middle fingers
    x1,y1 = lmlist[8][1:]
    #middle
    x2, y2 = lmlist[12][1:]

    #check if a finger is up


    cv2.imshow("Image", img)
    cv2.waitKey(1)

    #tip of index and middle finger
