import time

import cv2
import numpy as np
# import HandTrackingModule as htm
import mediapipe as mp

class handDetector():
    def __init__(self,mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.mpHands.Hands()
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,1,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLmrk in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLmrk,self.mpHands.HAND_CONNECTIONS)
        return img


    def findPosition(self,img,handNo=0, draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x *w), int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)
        return lmlist

def main():
    ptime = 0
    ctime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            print(lmlist[4])

        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime

        cv2.putText(img, str(int(fps)), (10 ,70), cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()



# main()