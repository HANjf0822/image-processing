import cv2
import numpy as np
import matplotlib.pyplot as plt


# gamma correction
def gamma_correction(img, c=1, g=2.2):
	out = img.copy()
	out /= 255.
	out = (1/c * out) ** (1/g)

	out *= 255
	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori_gamma.jpg").astype(np.float)
cv2.namedWindow('ori',0)
cv2.resizeWindow('ori',900,900)
cv2.imshow('ori',img)
# Gammma correction
out = gamma_correction(img)

# Save result
cv2.namedWindow('result',0)
cv2.resizeWindow('result',900,900)
cv2.imshow("result", out)
cv2.waitKey(0)