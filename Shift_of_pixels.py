import cv2
import numpy

img = cv2.imread('me.jpg')
col = img.shape[1]
row = img.shape[0]

M = numpy.float32([[1, 0, 500], [0, 1, 500]])       # along x axis with 500 pixels and y axis with 500 pixels
shifted = cv2.warpAffine(img, M, (col, row))        # map pixel within boundries
cv2.imwrite('shift_pixel.jpg', M)
img = cv2.resize(img, (700, 500))
cv2.imshow('shifted_image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

