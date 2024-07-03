import cv2
import time
import os
import handTrackingModel as htm


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0


imagepath = '/Users/maryammaksour/Desktop/ComputerVision/FingerCounter/images'
mylist = os.listdir(imagepath)
imglist = []

mylist.sort()
print(mylist)
for imgpath in mylist:
    image = cv2.imread(f'{imagepath}/{imgpath}')
    imglist.append(image)

detector = htm.HandDetector(detectionCon = 0.7)

def is_open(finger, lmlist):

    if finger == 4 :
        return lmlist[finger][1] < lmlist[finger-1][1]
    else:
        return lmlist[finger][2] < lmlist[finger-2][2]

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    lmlist = detector.findPosition(img, draw=False)

    cnt = 0
    if len(lmlist) > 0:
        # (4, 2), (8, 6), (12, 10), (16, 14), (20, 18)
        # we need to know if this finger is open or cloase 
        fingers = [4, 8, 12, 16, 20]


        for f in fingers:
            if is_open(f, lmlist):
                cnt += 1
            

    h, w, c = imglist[0].shape
    img[0:h , 0:w] = imglist[cnt]

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 460), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 200, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break