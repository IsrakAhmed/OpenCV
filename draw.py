import cv2
import numpy

blank = numpy.zeros((500,500,3), dtype='uint8')
cv2.imshow('Blank',blank)

# 1. Paint the image a certain colour

# blank[200:300, 300:400] = 0,0,255
# cv2.imshow('Red',blank)



# 2. Draw a Rectangle

cv2.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv2.FILLED)
# cv2.imshow('Rectangle', blank)



# 3. Draw a Circle

cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=2)
# cv2.imshow('Circle', blank)


# 4. Draw a Line

cv2.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv2.imshow("Line",blank)



# 5. Write Text

cv2.putText(blank, 'Hello There', (180,400), cv2.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), 2)
cv2.imshow("Text",blank)



cv2.waitKey(0)