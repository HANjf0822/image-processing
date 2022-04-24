import cv2
import numpy as np


# Dicrease color
def dicrease_color(img):
	out = img.copy()

	out = (out // 64)*64+32
	return out


# Read image
img = cv2.imread("imori.jpg")

# Dicrease color
out = dicrease_color(img)

cv2.namedWindow('result',0)
cv2.resizeWindow('result',900,900)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()