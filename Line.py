import cv2
import numpy

# line draw

img = cv2.imread('me.jpg')
cv2.line(img, (100, 100), (500, 100), (255, 255, 255), 10)
cv2.imwrite('line_in_img.jpg', img)
img = cv2.resize(img, (700, 500))
cv2.imshow('line_in_img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


