import cv2
import numpy as np

cap = cv2.VideoCapture('/Users/maryammaksour/Desktop/ComputerVision/Motion Filtering/1.mp4')

while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, (800, 400))

    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    # convert data from float to int in range [0, 255]
    laplacian  = np.uint8(laplacian)

    cv2.imshow("laplacian", laplacian)

    #                       threshold less ==> more edges
    edges = cv2.Canny(frame, 100, 100)
    cv2.imshow("Canny", edges)


    if cv2.waitKey(5) == ord('x'):
            break
    
cv2.destroyAllWindows()
cap.release()