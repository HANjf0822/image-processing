import cv2
import numpy as np
# #做灰度处理的方法，处理完之后就没有像素残留了
#
#
# # Gray scale
#
#
# def BGR2GRAY(img):
#     b = img[:, :, 0].copy()
#     g = img[:, :, 1].copy()
#     r = img[:, :, 2].copy()
#
#     # Gray scale
#     out = 0.2126 * r + 0.7152 * g + 0.0722 * b
#     out = out.astype(np.uint8)
#
#     return out
#
# # max-min filter
#
#
# def max_min_filter(img, K_size=3):
#     H, W = img.shape
#
#     # Zero padding
#     pad = K_size // 2
#     out = np.zeros((H + pad * 2, W + pad * 2))
#     out[pad: pad + H, pad: pad + W] = gray.copy()
#     tmp = out.copy()
#
#     # filtering
#     for y in range(H):
#         for x in range(W):
#             out[pad + y, pad + x] = np.max(tmp[y: y + K_size, x: x + K_size]) - np.min(tmp[y: y + K_size, x: x + K_size])
#
#     out = out[pad: pad + H, pad: pad + W].astype(np.uint8)
#
#     return out
#
#
# # Read image
# img = cv2.imread("imori.jpg")
#
# # grayscale
# gray = BGR2GRAY(img)
#
# # Max-Min filtering
# out = max_min_filter(gray, K_size=3)
#
# # Save result
# cv2.namedWindow('result',0)
# cv2.resizeWindow('result',900,900)
# cv2.imshow("result", out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 不用做Gray灰度值的变换的方法，处理之后的图片可能有点像素残留

def max_min_filter(img, K_size=3):

    H, W, C = img.shape


    # Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2,C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x,c] = np.max(tmp[y: y + K_size, x: x + K_size,c]) - \
                np.min(tmp[y: y + K_size, x: x + K_size,c])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# grayscale
# gray = BGR2GRAY(img)

# Max-Min filtering
out = max_min_filter(img, K_size=3)

# Save result
cv2.namedWindow('result',0)
cv2.resizeWindow('result',900,900)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.bitwise_not()是对图像进行取反操作！！！，从亮通道变成暗通道，从暗通道变成亮通道
# out1 = cv2.bitwise_not(out)
# cv2.namedWindow('result1',0)
# cv2.resizeWindow('result1',900,900)
# cv2.imshow('result1',out1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()