# mandrill1 reconstruction
import cv2
import numpy as np

# load image
img = cv2.imread("mandrill1.jpg")

blue = img[:, :, 1].copy()
blue = np.flip(blue)
