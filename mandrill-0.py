# apparently we can tell that the colour channels are swapped
# blue swapped to red, green swapped to blue and red swapped to green
from ctypes.wintypes import RGB
import cv2
import numpy as np
# load the image
img = cv2.imread("mandrill0.jpg")
# swapped the color channels 
red = img[:, :, 2].copy()
green = img[:, :, 0].copy()
blue = img[:, :, 1].copy()

img[:, :, 0] = red
img[:, :, 1] = green
img[:, :, 2] = blue

cv2.imwrite("mandrill-0.jpg", img)

