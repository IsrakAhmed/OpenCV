import cv2 as cv

# Resizing Photos

def rescaleFrame(frame, scale = 0.75):

    # This function works for Live Videos, Videos, Images

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



img = cv.imread('Resources/Photos/cat.jpg')

resized_img = rescaleFrame(img)

cv.imshow('Cat', img)
cv.imshow('Cat Resized', resized_img)

cv.waitKey(0)