import cv2
import numpy

img = cv2.imread('me.jpg')

smaller = cv2.pyrDown(img)

larger = cv2.pyrUp(img)


img = cv2.resize(img, (700, 500))
cv2.imshow('original', img)
smaller = cv2.resize(img, (700, 500))
cv2.imshow('smaller', smaller)
larger = cv2.resize(img, (700, 500))
cv2.imshow('larger', larger)

cv2.waitKey(0)
cv2.destroyAllWindows()