import cv2
import mediapipe as mp
import time
import math


class possDetector():

    def __init__(self, mode = False, upBody = False, smooth = True, 
                 detectionCon = 0.5, trackCon = 0.5):
        
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpPos = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils
        self.pose = self.mpPos.Pose()
        

    def findPose(self, img, draw = True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.result = self.pose.process(imgRGB)

            if draw and self.result.pose_landmarks:
                self.mpDraw.draw_landmarks(img, 
                                           self.result.pose_landmarks,
                                            self.mpPos.POSE_CONNECTIONS)

            return img
    
    def findPosition(self, img, draw = True):
        self.lmlist = []

        if self.result.pose_landmarks:
            self.mpDraw.draw_landmarks(img, self.result.pose_landmarks, self.mpPos.POSE_CONNECTIONS)
            for id, lm in enumerate(self.result.pose_landmarks.landmark):
                h, w, c = img.shape
                cx = int(lm.x*w)
                cy = int(lm.y*h)
                self.lmlist.append([ id, cx, cy ])

                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        

        return self.lmlist

    '''
    find the angle between 3 points
    '''
    def findAngel(self, img, p1, p2, p3, draw = True):
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]

        angel = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2) )

        if angel < 0:
             angel += 360


        if draw:
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
                cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 2)
                
                cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x1, y1), 15, (255, 0, 0), 1)

                cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (255, 0, 0), 1)

                cv2.circle(img, (x3, y3), 10, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x3, y3), 15, (255, 0, 0), 1)

                cv2.putText(img, str(int(angel)), (x2-20, y2+50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2 )
        return angel



def main():
    
    cap = cv2.VideoCapture('/Users/maryammaksour/Desktop/cv/Position/p1.mp4')
    pTime = 0
    
    detector = possDetector()
    

    while True:

        success, img = cap.read()

        img = detector.findPose(img)
        lmlist = detector.findPosition(img)

        print(lmlist)

        cTime = time.time()
        fps = 1 / (cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3 )
        cv2.imshow("Image", img)

        cv2.waitKey(1)

if __name__ == '__main__':
    main()