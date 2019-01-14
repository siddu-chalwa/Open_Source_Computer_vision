import cv2
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('me.jpg')
img = cv2.medianBlur(img, 5)
ret, threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
threshold2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
threshold3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
title = ['original img', 'global threshold', 'adaptive mean threshold', 'adaptive gaussian threshold']
images = [img, threshold1, threshold2, threshold3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imread(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])
plt.show()