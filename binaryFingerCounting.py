import cv2
import time
import os
import HandTrackingModule as htm

camWidth, camHeight = 720, 480

cap = cv2.VideoCapture(0)
cap.set(3,camWidth)
cap.set(4, camHeight)

detector = htm.handDetector(detectionCon=0.75)

value = 0

while True:
    #put a picture in that is 100x100 on the screen
    #h,w,c = image.shape
    #img [0:h, 0:w] = image



    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    value = 0
    #if a hand is seen
    if len(lmlist) != 0:
        #y position of the hand is the third element
        fingerTips = [(4,"Thumb",1),(8,"Pointer Finger",2),(12, "Middle Finger",4),(16, "Ring Finger",8),(20, "Pink",16)]
        #thumb case
        #need to check if the thumb is on the left or right side of the knuckle
        thumbUp = lambda pos: pos == 4 and lmlist[pos][1] < lmlist[pos-1][1]
        othersUp = lambda pos: lmlist[pos][2] < lmlist[pos-2][2]




        # res = [x for x in fingerTips if thumbUp(x[0]) or othersUp(x[0])]
        res = []
        for i in fingerTips:
            #thumb not being recognized
            if(i[0] == 4):
                if(lmlist[i[0]][1] > lmlist[i[0]-1][1]):
                    value += i[2]
                    res.append(i)
            else:
                if lmlist[i[0]][2] < lmlist[i[0] - 2][2]:
                    value += i[2]
                    res.append(i)
                # print(i)
                # if lmlist[i[0]][2] < lmlist[i[0]-2][2]:
                #     res.append(i)





        print(res)
        cv2.putText(img, str(value), (10,70), cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3)

        # if lmlist[8][2]  > lmlist[6][2]:
        #     print('pointer is down')


    cv2.imshow("Image", img)
    cv2.waitKey(1)