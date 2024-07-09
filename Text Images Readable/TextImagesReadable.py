import cv2

img = cv2.imread('/Users/maryammaksour/Desktop/ComputerVision/Text Images Readable/1.jpg')

# convert img to gray scalle
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#                               threshold, max color, algorithm
ret, result = cv2.threshold( img, 105, 255, cv2.THRESH_BINARY)
# evry color under threshold c = 0 else c = 1
'''
with binary threshold algorithem we can not use only one threshold 
for all image SO we need mor dynamic algorithem for that
'''
#                                         choce the threshold in dynamic way,          , block size (odd), const
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  cv2.THRESH_BINARY, 51, 8)


cv2.imshow("Image", img)
cv2.imshow("adaptive", adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()