import numpy
import cv2

# convet image format ex. jpg --> png

img = cv2.imread('me.jpg')
img = cv2.resize(img, (700, 600))
cv2.imwrite('change_extension.png', img)
cv2.imshow('change_extension', img)
cv2.waitKey(0)
cv2.destroyAllWindows()