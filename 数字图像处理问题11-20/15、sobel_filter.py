import cv2
import numpy as np

# Gray scale
def BGR2GRAY(img):
	b = img[:, :, 0].copy()
	g = img[:, :, 1].copy()
	r = img[:, :, 2].copy()

	# Gray scale
	out = 0.2126 * r + 0.7152 * g + 0.0722 * b
	out = out.astype(np.uint8)

	return out


# sobel filter
def sobel_filter(img, K_size=3):
# 	if len(img.shape) == 3:
# 		H, W, C = img.shape
# 	else:
# 		img = np.expand_dims(img, axis=-1)
	H, W, C = img.shape

	# Zero padding
	pad = K_size // 2
	out = np.zeros((H + pad * 2, W + pad * 2,C), dtype=np.float)
	out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
	tmp = out.copy()

	out_v = out.copy()
	out_h = out.copy()

	## Sobel vertical
	Kv = [[1., 2., 1.],[0., 0., 0.], [-1., -2., -1.]]
	## Sobel horizontal
	Kh = [[1., 0., -1.],[2., 0., -2.],[1., 0., -1.]]

	# filtering
	for y in range(H):
		for x in range(W):
			for c in range(C):
				out_v[pad + y, pad + x,c] = np.sum(Kv * (tmp[y: y + K_size, x: x + K_size,c]))
				out_h[pad + y, pad + x,c] = np.sum(Kh * (tmp[y: y + K_size, x: x + K_size,c]))

	out_v = np.clip(out_v, 0, 255)
	out_h = np.clip(out_h, 0, 255)

	out_v = out_v[pad: pad + H, pad: pad + W].astype(np.uint8)
	out_h = out_h[pad: pad + H, pad: pad + W].astype(np.uint8)

	return out_v, out_h

# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# grayscale
# gray = BGR2GRAY(img)

# sobel filtering
out_v, out_h = sobel_filter(img, K_size=3)

# Save result
cv2.namedWindow('result_v',0)
cv2.resizeWindow('result_v',900,900)
cv2.imshow("result_v", out_v)
cv2.waitKey(0)
# while cv2.waitKey(100) != 27:# loop if not get ESC
#     if cv2.getWindowProperty('result_v',cv2.WND_PROP_VISIBLE) <= 0:
#         break
cv2.destroyWindow('result_v')

cv2.namedWindow('result_h',0)
cv2.resizeWindow('result_h',900,900)
cv2.imshow("result_h", out_h)
cv2.waitKey(0)
# loop if not get ESC or click x
# while cv2.waitKey(100) != 27:
#     if cv2.getWindowProperty('result_h',cv2.WND_PROP_VISIBLE) <= 0:
#         break
cv2.destroyWindow('result_h')
# cv2.destroyAllWindows()