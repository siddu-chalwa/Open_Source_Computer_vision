
# erosion --> decrease of image
# dialotion --> increase of image
# and both of them will eliminate holes or extra small portoin

import cv2
import numpy as np

img = cv2.imread('me.jpg')
img = cv2.resize(img, (700, 500))
cv2.imshow('original', img)
cv2.waitKey(0)

kernal = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernal, iterations=1)
erosion = cv2.resize(img, (700, 500))
cv2.imshow('erosion', erosion)
cv2.waitKey(0)

dilaton = cv2.dilate(img, kernal, iterations=1)
dilaton = cv2.resize(img, (700, 500))
cv2.imshow('dilation', dilaton)
cv2.waitKey(0)

# opening and closing

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
cv2.imshow('Opening', opening)
cv2.waitKey(0)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
