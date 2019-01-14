#shape size and dtype

import cv2
import numpy

img = cv2.imread('me.jpg')
print(img.shape)            # return dimension
print(img.size)             # no. of pixels
print(img.dtype)            # type of image
