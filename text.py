import cv2
import numpy

# inserting text over image
img = cv2.imread('me.jpg')
cv2.putText(img, 'Siddu Chalwa', (50, 1800), cv2.FONT_HERSHEY_DUPLEX, 5, (255, 255, 255), 10, cv2.LINE_8)
cv2.imwrite('text_in_img.jpg', img)
img = cv2.resize(img, (700, 500))
cv2.imshow('text_in_img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

