import cv2
import mediapipe as mp
import time



class HandDetector():
   def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5,modelComplexity = 1, trackCon = 0.5 ):
      
      self.mode = mode
      self.maxHands = maxHands
      self.modelComplex = modelComplexity
      self.detectionCon = detectionCon
      self.trackCon = trackCon

      self.mpHands = mp.solutions.hands
      # only RGB image
      self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                       self.detectionCon, self.trackCon)
      # to draw  on hand
      self.mpDraw = mp.solutions.drawing_utils

   def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        
        # cheack if we have multy hands
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)
            
        return img

   def findPosition(self, img, handNo=0, draw=True):
                
            lmlist = []

            if self.results.multi_hand_landmarks:
                myHand = self.results.multi_hand_landmarks[handNo]
                
                for id, lm in enumerate(myHand.landmark):
                    #print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)

                    lmlist.append([id, cx, cy])
                    
                    if draw:
                        cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

            return lmlist

def main():
    
   # pre time
    pTime = 0
    # curr time
    cTime = 0

    cap = cv2.VideoCapture(0)
    det = HandDetector()

    while True:
        success, img = cap.read() 

        img = det.findHands(img)
        lmlist = det.findPosition(img)

        if len(lmlist) != 0:
            print(lmlist[8])


        # create fram per second
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        #                                  pos          font              size  color       thex
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)

        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
  main()