import cv2 as cv

# Reading Videos

capture = cv.VideoCapture(0)    # Reading Webcam

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()