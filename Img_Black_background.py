# black 3x3 image form
import numpy
import cv2

img = numpy.zeros((1024, 1024), dtype=numpy.uint8)      # 1024, 1024 --> dimensoin and uint8 --> 8 bits of 1 pixel
img = cv2.resize(img, (700, 500))
print(img)      # print image value
cv2.imwrite('Img_Black_background.jpg', img)       # write image
cv2.imshow('Img_Black_background', img)      # image display
cv2.waitKey(0)          # wait till u enter any key
cv2.destroyAllWindows()     # close all windows