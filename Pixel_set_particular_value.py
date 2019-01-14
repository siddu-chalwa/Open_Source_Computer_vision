# accessing image data with numpy array

import cv2
import numpy


img = cv2.imread('me.jpg')         # image read
for i in range(100):                # set 0:100, 0:300 as 255(white)
    for j in range(300):
        img[i, j] = [255, 255, 255]
cv2.imwrite('Set_Pixel.jpg', img)
img = cv2.resize(img, (700, 500))
cv2.imshow('set_pixel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# to print particular pixel value
img1 = cv2.imread('me.jpg')
print(img1.item(150, 120, 0))

# to set particular pixel value
img1.itemset((150, 120, 0), 255)
print(img1.item(150, 120, 0))

