# Import Necessary library
import cv2
import numpy as np

# Load input image and convert to grayscale
image = cv2.imread('puzzle.jpg',cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Load template image
template = cv2.imread('waldo.jpeg', 0)
# Match Template and grayscaled image
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
# Find min and val of location and value
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# Set Dimensions for box
top_left = max_loc
bottom_right = (top_left[0]+50, top_left[1]+50)
# Create Bounding box
cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 5)
# Saved output image
cv2.imwrite("Findwaldo.jpg", image)