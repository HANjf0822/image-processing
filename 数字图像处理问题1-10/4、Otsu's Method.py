import cv2 as cv
import numpy as np
#Gray_change
def BGR2GRAY(img):
	b = img[:, :, 0].copy()
	g = img[:, :, 1].copy()
	r = img[:, :, 2].copy()

	# Gray scale
	out = 0.2126 * r + 0.7152 * g + 0.0722 * b
	out = out.astype(np.uint8)

	return out
#otsu_Binarization
def otsu_binarization(img,th=128):
    max_sigma = 0
    max_t = 0

    # determine threshold 自动决定阈值
    for _t in range(1, 255):
        v0 = out[np.where(out < _t)]
        m0 = np.mean(v0) if len(v0) > 0 else 0.
        w0 = len(v0) / (H * W)
        v1 = out[np.where(out >= _t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0.
        w1 = len(v1) / (H * W)
        sigma = w0 * w1 * ((m0 - m1) ** 2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t

    # Binarization
    print("threshold =", max_t)
    th = max_t
    out[out < th] = 0
    out[out >= th] = 255

    return out

    # Read image


img = cv.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# Grayscale
out = BGR2GRAY(img)

# Otsu's binarization
out = otsu_binarization(out)

# Save result
# cv.imwrite("out.jpg", out)
cv.namedWindow('Otus_result',0)
cv.resizeWindow('Otus_result',900,900)
cv.imshow("Otus_result", out)
cv.waitKey(0)
cv.destroyAllWindows()