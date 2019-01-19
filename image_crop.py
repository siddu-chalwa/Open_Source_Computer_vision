import  cv2
import numpy

img = cv2.imread('me.jpg')

height, width = img.shape[:2]

start_row, start_col = int(height * .25), int(width * .25)
end_row, end_col = int(height * .65), int(width * .65)

cropped = img[start_row:end_row, start_col:end_col]


img = cv2.resize(img, (700, 500))
cv2.imshow('original img', img)
cv2.waitKey(0)
cropped = cv2.resize(cropped, (700, 500))
cv2.imshow('cropped img', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()

