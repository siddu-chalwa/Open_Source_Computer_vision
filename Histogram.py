import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('me.jpg')

plt.hist(img.ravel(), 256, [0, 256])
plt.show()


color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histogram2 = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])

plt.show()