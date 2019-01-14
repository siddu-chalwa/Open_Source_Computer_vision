import cv2
import numpy

# face detection using webcam
video_capture = cv2.VideoCapture(0)     # video stream

while 1:
    ret, pic = video_capture.read()
    faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml').detectMultiScale(pic, 1.3, 5)   #1, 3 --> scale factor, min neighbor

    for(x, y, w, h) in faces:
        cv2.rectangle(pic, (x, y), (x+w, y+h), (255, 255, 255), 6)
        cv2.putText(pic, 'me', (x, y), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2, cv2.LINE_8)

    print('No. of faces: {}'.format(len(faces)))
    cv2.imshow('face', pic)
    k = cv2.waitKey(0) & 0xFF
    if k == 2:
        break
cv2.destroyAllWindows()