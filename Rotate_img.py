import cv2
import numpy

img = cv2.imread('me.jpg')
col = img.shape[1]
row = img.shape[0]
center = (col/2, row/2)
angle = 180
M = cv2.getRotationMatrix2D(center, angle, 1)  # 1 --> scale
rotate = cv2.warpAffine(img, M, (col, row))

cv2.imwrite('rotate_img.jpg', rotate)
img = cv2.resize(rotate, (700, 500))
cv2.imshow('rotated_image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
