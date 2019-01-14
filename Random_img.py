# random pixels with array

import cv2
import numpy
import os


array = bytearray(os.urandom(180000))       # os --> operating system, 120000 --> pixels
array_represent = numpy.array(array)

# reshape to random array and represent in gray and RGB

gray_img = array_represent.reshape(600, 300)            # 400x300 = 120000
cv2.imwrite('random_gray_img.jpg', gray_img)
cv2.imshow('random_gray_img', gray_img)
BRG_img = array_represent.reshape(300, 200, 3)
cv2.imwrite('random_color_img.jpg', BRG_img)
cv2.imshow('random_color_img', BRG_img)

cv2.waitKey(0)
cv2.destroyAllWindows()




