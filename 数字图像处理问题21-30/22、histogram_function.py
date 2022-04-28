import cv2
import numpy as np
import matplotlib.pyplot as plt


# histogram manipulation
def hist_mani(img, m0=128, s0=52):
	m = np.mean(img)
	s = np.std(img)

	out = img.copy()

	# normalize
	out = s0 / s * (out - m) + m0
	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori_dark.jpg")
cv2.namedWindow('ori',0)
cv2.resizeWindow('ori',900,900)
cv2.imshow('ori',img)

out = hist_mani(img)
# print(np.mean(out))
# print(np.std(out))

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.show()

# Save result
cv2.namedWindow('result',0)
cv2.resizeWindow('result',900,900)
cv2.imshow("result", out)
cv2.waitKey(0)