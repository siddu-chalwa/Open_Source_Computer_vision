import cv2
import numpy
from PIL import Image

img = cv2.imread('imgT.jpg', 0)                          # read image and 0 --> grey scale image
(T_value, img_threshold) = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)         # 200, 255 --> threshold value, max value, threshold binary --> type
cv2.imwrite('img_threshold.jpg', img_threshold)         # write image
Image.open('img_threshold.jpg').show()                  # open image
