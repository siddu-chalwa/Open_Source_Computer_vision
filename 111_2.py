import cv2
import os
import numpy as np
import use as fr

test_img = cv2.imread("/home/ubuntu/Desktop/sid.jpg")
faces_detected, gray_img = fr.faceDetection(test_img)
print("face_Detected", faces_detected)

faces, faceID = fr.labels_for_training_data('/home/ubuntu/Desktop/trainingimages/')
face_recognizer = fr.train_classifier(faces, faceID)
name = {0 : "Siddu_Chalwa", 1 : "Shivanand_Chidri"}

for faces in faces_detected:
	(x, y, w, h) = face
	roi_gray = gray_img[y : y+h, x : x+h]
	label, confidence = face_recognizer.predict(roi_gray)
	print("confidence: ", confidence)
	print("label: ", label)
	fr.draw_rect(test_img, face)
	predicted_name = name[label]
	fr.puttext(test_img, predicted_name, x, y)
	

'''
for(x, y, w, h) in face_detected:
        cv2.rectangle(img_read, (x, y), (x+w, y+h), (255, 255, 255), 10)
'''
resize_img = cv2.resize(test_img, (700, 500))
cv2.imshow("face_recorgnize_image", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows



