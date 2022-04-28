import cv2
import numpy as np
import matplotlib.pyplot as plt


# histogram normalization
def hist_normalization(img, a=0, b=255):
    # get max and min
    c = img.min()
    d = img.max()

    out = img.copy()

    # normalization
    out = (b - a) / (d - c) * (out - c) + a
    # out[out < a] = a
    # out[out > b] = b
    out = out.astype(np.uint8)

    return out


# Read image
img = cv2.imread("imori_dark.jpg")
cv2.namedWindow('ori',0)
cv2.resizeWindow('ori',900,900)
cv2.imshow("ori",img)
H, W, C= img.shape

# histogram normalization
out = hist_normalization(img)

# Display histogram
plt.hist(img.ravel(), bins=255, rwidth=0.8, range=(0,255))
plt.show()
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.show()

# Save result
cv2.namedWindow('result',0)
cv2.resizeWindow('result',900,900)
cv2.imshow("result", out)
cv2.waitKey(0)