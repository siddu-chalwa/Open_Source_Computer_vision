import cv2
import numpy as np


image = cv2.imread('me.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Creating our 3 x 3 kernel
kernel_3x3 = np.ones((3, 3), np.float16) / 9

#print(kernel_3x3)
# We use the cv2.fitler2D to conovlve the kernal with an image

blurred = cv2.filter2D(image, -1, kernel_3x3, None)
cv2.imshow('3x3 Kernel Blurring', blurred)
cv2.waitKey(0)