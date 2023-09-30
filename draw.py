import cv2
import numpy

blank = numpy.zeros((500,500,3), dtype='uint8')
cv2.imshow('Blank',blank)

# 1. Paint the image a certain colour

blank[200:300, 300:400] = 0,0,255
cv2.imshow('Red',blank)

cv2.waitKey(0)