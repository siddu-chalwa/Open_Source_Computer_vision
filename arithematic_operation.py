import cv2
import numpy

img = cv2.imread('me.jpg')
M = numpy.ones(img.shape, dtype='uint8')

cv2.imshow('added_img', (cv2.resize(cv2.add(img, M), (700, 500))))
cv2.waitKey(0)
cv2.destroyAllWindows()
