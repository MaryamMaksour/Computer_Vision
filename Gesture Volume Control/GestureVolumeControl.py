'''
change voice valume using your hands
'''

import cv2
import numpy as np
import time
import handTrackingModel as htm
import math

import applescript

###########Video Capture Parameter############
wCam, hCam = 640, 480
##############################################

###########Voice Parameter####################
mnVol, mxVol = 0, 100
mn, mx = 18, 180

VolInfoD = applescript.AppleScript("get volume settings").run()
VolInfoL = list(VolInfoD.keys())

vol = (VolInfoD[VolInfoL[0]])
volBar = int(vol) 
length = int(vol)+ 400

volBar = np.interp(length, [mn, mx], [400, 150])


##############################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.HandDetector(detectionCon = 0.7)

def change_valume(target_volume):

    applescript.AppleScript(f'set volume output volume {target_volume}').run()


while True:

    success, img = cap.read()

    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw = False)

    

    if len(lmlist) > 0:
        # we need lm pint 4 and 8
        #print(lmlist[4], lmlist[8])

        x1, y1 = lmlist[4][1:]
        x2, y2 = lmlist[8][1:]
        # center for line between (x1, y1) and (x2, y2)
        cx, cy = (x1+x2)//2, (y1 + y2)//2

        cv2.circle(img, (x1, y1), 8, (0, 200, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 8, (0, 200, 0), cv2.FILLED)

        #create line 
        cv2.line(img, (x1, y1), (x2, y2), (200, 0, 0), 2)
        cv2.circle(img, (cx, cy), 5, (0, 200, 0), cv2.FILLED)

        # length of line
        length = math.hypot(x2-x1, y2-y1)
        #print(length)
        mx = 180
        mn = 18

        if length <= mn:
            cv2.circle(img, (cx, cy), 8, (155, 100, 0), cv2.FILLED)
        if length >= mx:
            cv2.circle(img, (cx, cy), 8, (0, 100, 155), cv2.FILLED)

        vol = np.interp(length, [mn, mx], [mnVol, mxVol])
        volBar = np.interp(length, [mn, mx], [400, 150])
        

        if vol:
            change_valume(int(vol))

    # valume rectangle
    cv2.rectangle(img, (50, 150), (85, 400), (30, 188, 270), 2)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (30, 188, 270), cv2.FILLED)
    cv2.putText(img, f'{int(vol)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 255, 0), 2)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

