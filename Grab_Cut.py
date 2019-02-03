import cv2
import numpy

img = cv2.imread('me.jpg')

mask = numpy.zeros(img.shape[:2], numpy.uint8)

bgdModel = numpy.zeros((1, 65), numpy.float64)
fgdModel = numpy.zeros((1, 65), numpy.float64)

rect = (250, 50, 421, 600)
# GrabCut algorithm specifying the empty models and mask
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
# The values, 0 and 2, will be converted into zeros, and 1-3 into ones, and stored into mask2
mask2 = numpy.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img*mask2[:, :, numpy.newaxis]
# Store image as Grabcut.jpg
cv2.imwrite("Grabcut.jpg", img)
