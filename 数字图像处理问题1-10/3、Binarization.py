import cv2 as cv
import numpy as np
def Gray_change(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()
    out = 0.2126*r+0.7152*g+0.0722*b
    out = out.astype(np.uint8)
    return out

def Binarization(img):
    img[img<128] = 0
    img[img>=128] = 255
    return img
img = cv.imread('imori.jpg')
out = Gray_change(img)
out = Binarization(out)

cv.namedWindow('Binarization_result',0)
cv.resizeWindow('Binarization_result',900,900)
cv.imshow('Binarization_result',out)
cv.waitKey(0)
cv.destroyAllWindows()

