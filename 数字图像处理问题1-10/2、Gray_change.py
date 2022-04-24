import cv2 as cv
import numpy as np

def Gray_change(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()
    out = 0.2126*r+0.7152*g+0.0722*b
    out = out.astype(np.uint8)
    return out

img = cv.imread('imori.jpg')
out = Gray_change(img)

cv.namedWindow('Gray_change',0)
cv.resizeWindow('Gray_change',900,900)
cv.imshow('Gray_change',out)

cv.waitKey(0)
cv.destroyAllWindows()