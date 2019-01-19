# image blending

import cv2
import numpy


# remember that size of both the images need to be same
img1 = cv2.imread('me.jpg')
img1 = cv2.resize(img1, (700, 500))
img2 = cv2.imread('PM.jpg')
img2 = cv2.resize(img2, (700, 500))

val1 = cv2.add(img1, img2)
val2 = cv2.addWeighted(img1, 0.7, img2, 0.7, 0)

cv2.imshow('add_image1', val1)
cv2.imshow('add_image2', val2)
cv2.waitKey(0)
cv2.destroyAllWindows()