import  cv2
import numpy as na


# use of multiple pixel

img = cv2.imread('me.jpg')
img[:, :, 1] = 0               # 1 --> channel varies from 0 to 2
cv2.imwrite('Multiple_pixel.jpg', img)
img = cv2.resize(img, (700, 500))
cv2.imshow('Multiple_pixel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
