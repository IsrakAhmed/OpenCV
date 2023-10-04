import cv2
import numpy

blank = numpy.zeros((500,500,3), dtype='uint8')
cv2.imshow('Blank',blank)

# 1. Paint the image a certain colour

# blank[200:300, 300:400] = 0,0,255
# cv2.imshow('Red',blank)



# 2. Draw a Rectangle

cv2.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv2.FILLED)
cv2.imshow('Rectangle', blank)



cv2.waitKey(0)