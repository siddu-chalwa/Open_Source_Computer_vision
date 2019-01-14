import cv2
import numpy
from PIL import Image

# differentiate black and while at edges

img = cv2.imread('imgT.jpg')
img_detection = cv2.Canny(img, 50, 100)      # threshold1, threshold2
cv2.imwrite('Img_Edge_Detection.jpg', img_detection)
Image.open('Img_Edge_Detection.jpg').show()

