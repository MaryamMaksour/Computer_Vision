import cv2


vedio = cv2.VideoCapture('/Users/maryammaksour/Desktop/ComputerVision/Motion Filtering/1.mp4')

subtractor = cv2.createBackgroundSubtractorMOG2(300, 50)

while True:
    ret, frame = vedio.read()

    if ret:
        mask = subtractor.apply(frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(5) == ord('x'):
            break
    else: 
        vedio = cv2.VideoCapture('/Users/maryammaksour/Desktop/ComputerVision/Motion Filtering/1.mp4')


cv2.destroyAllWindows()
vedio.release()