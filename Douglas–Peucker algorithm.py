# Import Necessary library
import cv2
import numpy as np

# Read Input image
img = cv2.imread("me.jpg", 1)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image to remove noise
blur = cv2.blur(gray, (3, 3))
# Obtain thresholding between 50 and 255 intensity
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
# Finding contours for the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Create hull array for convex hull points
hull = []
# Calculate points for each contour
for i in range(len(contours)):
    # Creating Convex Hull object for each contour
    hull.append( cv2.convexHull(contours[i], False))

# Create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
# draw contours and hull points
for i in range(len(contours)):
    # green - color for contours
     color_contours = (0, 255, 0)
     # Blue - color for convex hull
     color = (255, 0, 0)
     # Draw its contour
     cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
     # Draw its convex hull object
     cv2.drawContours(drawing, hull, i, color, 1, 8)


# Draw all the contours in image
cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
# Save image as contour1.jpg
cv2.imwrite("convexHull.jpg", img)