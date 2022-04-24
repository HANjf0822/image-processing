import cv2 as cv
img = cv.imread("imori.jpg")

#查看RGB通道对应的函数通道
# blue = img[:,:,0].copy()
# green = img[:,:,1].copy()
# red = img[:,:,2].copy()
# cv.namedWindow('blue_channel',0)
# cv.resizeWindow('blue_channel',700,900)
# cv.imshow("blue_channel",blue)
#
# cv.namedWindow('green_channel',0)
# cv.resizeWindow('green_channel',700,900)
# cv.imshow("green_channel",green)
#
# cv.namedWindow('red_channel',0)
# cv.resizeWindow('red_channel',700,900)
# cv.imshow("red_channel",red)
# cv.waitKey()
# cv.destroyAllWindows()

#写一个函数可以将图像的通道BGR->RGB的
def BGR2RGB(img):
    blue = img[:,:,0].copy()
    green = img[:,:,1].copy()
    red = img[:,:,2].copy()

    img[:,:,0] = red
    img[:,:,1] = green
    img[:,:,2] = blue
    return img
img1 = img

cv.namedWindow('originl_result',0)
cv.resizeWindow('originl_result',900,900)
cv.imshow('originl_result',img1)

img2 = BGR2RGB(img)

cv.namedWindow('change_result',0)
cv.resizeWindow('change_result',900,900)
# cv.imwrite('out.jpg',img2)
cv.imshow('change_result',img2)

cv.waitKey(0)
cv.destroyAllWindows()
