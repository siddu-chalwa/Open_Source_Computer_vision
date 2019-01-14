import cv2
import numpy
from PIL import Image

img = cv2.imread('imgT.jpg')                # image read
blur = cv2.GaussianBlur(img, (7, 7), 0)     # smoothining or bluring of image, there are 4 tech, one is gaussianBlur
cv2.imwrite('Img_Blur_Gaussian.jpg', blur)           # image write
Image.open('Img_Blur_Gaussian.jpg').show()           # image open
