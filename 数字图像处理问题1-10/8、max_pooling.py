import cv2
import numpy as np


# average pooling
def average_pooling(img, G=4):
    out = img.copy()

    H, W, C = img.shape
    #print(H,W,C)
    Nh = int(H / G)
    Nw = int(W / G)
    print(Nh,Nw)

    for y in range(Nh):
        for x in range(Nw):
            for c in range(C):
                out[G * y:G * (y + 1), G * x:G * (x + 1), c] = np.max(out[G * y:G * (y + 1), G * x:G * (x + 1), c])

    return out


# Read image
img = cv2.imread("imori.jpg")

# Average Pooling
out = average_pooling(img)

# Save result
cv2.namedWindow('result',0)
cv2.resizeWindow('result',900,900)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()