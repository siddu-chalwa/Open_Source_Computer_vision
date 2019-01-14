# overlap of image

import cv2
import numpy


img1 = cv2.imread('me.jpg')
img2 = img1[:, 0:200]
img1[:, 200:400] = img2
cv2.imwrite('Copy_Paste_imgPart.jpg', img1)
img = cv2.resize(img1, (700, 500))
cv2.imshow('copy_paste_pixel',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

