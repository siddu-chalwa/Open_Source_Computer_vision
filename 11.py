import cv2
import os
import numpy as np

def faceDetection(img_read):
        gray_img = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
        face_classifier = cv2.CascadeClassifier('/home/ubuntu/Open_Source_Computer_vision/haarcascade_frontalface_default.xml')
        faces_detected = face_classifier.detectMultiScale(gray_img, scaleFactor = 1.32, minNeighbors = 5)
        return faces_detected, gray_img

img_read = cv2.imread("/home/ubuntu/Desktop/S3.jpg")
face_detected, gray_img = faceDetection(img_read)
print("face_Detected", face_detected)

for(x, y, w, h) in face_detected:
        cv2.rectangle(img_read, (x, y), (x+w, y+h), (255, 255, 255), 10)

resize_img = cv2.resize(img_read, (475, 680))
cv2.imwrite("/home/ubuntu/Desktop/face_detected_image_3.jpg", resize_img)
cv2.imshow("face_detected_image_3", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows


