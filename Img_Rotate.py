import cv2
import numpy
from PIL import Image

pic = cv2.imread('imgT.jpg')                   #image is read
row = pic.shape[1]                            #Image dimensions/boundaries
col = pic.shape[0]
center = (col/2, row/2)                        #from where u want to rotate
angle = 90                                    #at what angle u want to rotate
M = cv2.getRotationMatrix2D(center, angle, 1)   #1 --> scale
rotate = cv2.warpAffine(pic, M, (col, row))      #transation and mapping

cv2.imwrite('Img_Rotate.jpg', rotate)            #write image
Image.open('Img_Rotate.jpg').show()             #open image and show
