import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('me.jpg')

# global threshold
ret, threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# otsu's threshold
ret, threshold2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img, 0, threshold1, 0, threshold2, 0]
title = ['original image', 'histogram', 'global threshold', 'histogrma', 'otsus image', 'histogram']

for i in range(3):
    plt.subplot(3, 2, i), plt.imshow(images[i], 'gray'), plt.title(images[i]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 2, i+1), plt.hist(images[i].ravel(), 256)
plt.show()