import cv2
import numpy
from PIL import Image

img = cv2.imread('imgT.jpg')    # image read
# central pixel is replaced with median value

img_blur = cv2.medianBlur(img, 3)   # 3 --> size
cv2.imwrite('Img_Blur_Median.jpg', img_blur)

Image.open('Img_Blur_Median.jpg').show()


