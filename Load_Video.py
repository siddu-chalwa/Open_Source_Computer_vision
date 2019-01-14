import cv2
import numpy

video = cv2.VideoCapture('s_job.mp4')       # read image

while(video.isOpened()):                    # till video remains open
    ret, frame = video.read()               # read frames
    cv2.imshow('video', frame)              # show video
    if cv2.waitKey(1) & 0xFF == ord('q'):   # wait for response from keyboard
        break
video.release()                             # close opened vidoe
cv2.destroyAllWindows()

