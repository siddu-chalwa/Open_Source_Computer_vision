import numpy
import cv2

# cap = cv2.VideoCapture(0)       if laptop then its camera or primary camera connected

cap = cv2.VideoCapture('s_job.mp4')

while(True):
    # capture frame by frame
    ret, frame = cap.read()

    # operation on frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    # display the resulting image
    cv2.imshow('frame', gray)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()