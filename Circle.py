import cv2
import numpy

# circle drawing

img = cv2.imread('me.jpg')
cv2.circle(img, (1200, 700), 650, (255, 255, 255), 10)
cv2.imwrite('circle_in_img.jpg', img)
img = cv2.resize(img, (700, 500))
cv2.imshow('circle in image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
