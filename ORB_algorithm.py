import cv2
import numpy

image = cv2.imread('place.jpg', cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create(1000, 1.2)

keypoints, descriptors = orb.detectAndCompute(image, None)
print("no of keypoints detedcted: ", len(keypoints))

image = cv2.drawKeypoints(image, keypoints, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite("ORB.jpg", image)
