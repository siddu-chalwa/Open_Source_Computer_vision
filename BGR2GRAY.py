import numpy
import cv2

img = cv2.imread('me.jpg', cv2.COLOR_BGR2BGRA)      # converting color image to gray while reading image
img = cv2.resize(img, (700, 500))                   # set a dimension of image
cv2.imwrite('BGR2GRAY.jpg', img)                    # write image
cv2.imshow('BGR2GRAY', img)                         # display image
cv2.waitKey()
cv2.destroyAllWindows()


# IMREAD_ANYCOLOR = 4    return any color
# IMREAD_UNCHANGED = -1    no change
# IMREAD_ANYDEPTH = 2      return 16 or 32 bit image or convert to 8 bit
