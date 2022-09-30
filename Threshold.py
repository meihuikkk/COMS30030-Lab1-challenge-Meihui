
# threshold_greyscale
import cv2
import numpy as np

# load the image mandrill.jpg in greyscale mode
image = cv2.imread("mandrill.jpg", 0)

# create mask for thr = 128
threshold = 128
# threshold = 150

# looping through all the pixels
# setting pixels with value > 128 to 255
for y in range(0, image.shape[0]): 
	for x in range(0, image.shape[1]):  
		if image[y, x] > 128:
			image[y, x] = 255
		else:
			image[y, x] = 0

# comparing with the built in function
image_1 = cv2.imread("mandrill.jpg", 0)
cv2.threshold(image_1, 128, 255, 1)

# save the image
cv2.imwrite("threshold.jpg", image)
cv2.imwrite("threshold_builtin.jpg", image_1)
