# Import Necessary library
import cv2
import numpy as np

# Read Input image
img = cv2.imread('board.webp')
# convert to grayscale
gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
# Edge Detection using canny
edges = cv2.Canny( gray, 50, 120)
# Define threshold Line Length and Line gap
minLineLength = 20
maxLineGap = 5
# Obtain Hough Lines
lines = cv2.HoughLinesP( edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
# Loop though the lines and draw them
for i in range(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line( img, (x1,y1), (x2,y2), (0,255,0),2)


# Display Output Image
cv2.imwrite("Houghedges.jpg", edges)
cv2.imwrite("Houghlines.jpg", img)