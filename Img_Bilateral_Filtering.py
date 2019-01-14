import numpy
import cv2
from PIL import Image

# preserve edges while smoothining

img = cv2.imread('imgT.jpg')        # image read

img_filter = cv2.bilateralFilter(img, 7, 100, 100,) # 7, 100, 100 --> dimension, sigmacolor, sigmaspace
cv2.imwrite('Img_Bilateral_Filter.jpg', img_filter)
Image.open('Img_Bilateral_Filter.jpg').show()