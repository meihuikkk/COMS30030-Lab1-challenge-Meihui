# threshold_colorscale
import cv2
from cv2 import imread
import numpy as np
# load the image file in color scale
image = cv2.imread("mandrillRGB.jpg")

# set the threshold to be thr = 200
thr  = 210
for y in range(0, image.shape[0]):  # go through all rows (or scanlines)
	for x in range(0, image.shape[1]):  # go through all columns
		pixelBlue = image[y, x, 0]
		pixelGreen = image[y, x, 1]
		pixelRed = image[y, x, 2]
		if pixelBlue > thr or pixelRed > thr:
			image[y, x, 0] = 255
			image[y, x, 1] = 255
			image[y, x, 2] = 255
		else:
			image[y, x, 0] = 0
			image[y, x, 1] = 0
			image[y, x, 2] = 0

# store the processed image
cv2.imwrite("thres_RGB.jpg", image)
