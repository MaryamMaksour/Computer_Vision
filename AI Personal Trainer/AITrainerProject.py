import cv2
import numpy as np
import time
import pasitionModel as pm

cap = cv2.VideoCapture('/Users/maryammaksour/Desktop/ComputerVision/AI Personal Trainer/1.mp4')

detector = pm.possDetector()
cnt = 0
dir = 0 # dir = 0 up , dir = 1 down

pTime = 0

while True:
    
    success , img = cap.read()
    #img = cv2.imread('/Users/maryammaksour/Desktop/ComputerVision/AI Personal Trainer/videos/images/push-angle.jpeg')
    img = cv2.resize(img, (1000, 500))

    img = detector.findPose(img, draw = False)
    lmlist = detector.findPosition(img, draw = False)
    
    if len(lmlist) > 0:
        # right hand
        #img = detector.findAngel(img, 12, 14, 16)
        # left hand
        
        angel = detector.findAngel(img, 11, 13, 15)

        # convert range to [0, 100]
        per = np.interp(angel, (190, 320), (0, 100))

        # check for the dumbbell curls
        if per == 100:
            if dir == 0:
                cnt += 0.5

            dir = 1
        
        if per == 0:
            if dir == 1:
                cnt += 0.5
            
            dir = 0



        cv2.putText(img, f'{int(cnt)}', (30, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5 )

        cTime = time.time()
        fps = 1 / (cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3 )
        

    cv2.imshow("V", img)
    cv2.waitKey(1)