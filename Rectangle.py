import cv2
import numpy

# drawing rectangle

img = cv2.imread('me.jpg')
cv2.rectangle(img, (600, 100), (1800, 1600), (255, 255, 255), 10)   # x1, y1 and x2, y2 and  10 represent thickness of rectangle
cv2.imwrite('rectangle_in_img.jpg', img)
img = cv2.resize(img, (700, 500))
cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




