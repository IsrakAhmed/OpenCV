import cv2
import numpy

blank = numpy.zeros((500,500), dtype='uint8')
cv2.imshow('Dummy',blank)

img = cv2.imread('Resources/Photos/cat.jpg')
cv2.imshow('Cat',img)


cv2.waitKey(0)