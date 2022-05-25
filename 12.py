import cv2
import numpy as np
import matplotlib.pyplot as plt


img_gray0 = cv2.imread("bridge.jpg", cv2.IMREAD_GRAYSCALE)
img_gray0 = 255 - img_gray0
h, w = img_gray0.shape

img_gray0 = cv2.resize(img_gray0, (w//2, h//2))

h, w = img_gray0.shape

plt.figure()
plt.imshow(img_gray0, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))

img_gray_eq = img_gray0

img_dither = np.zeros((h+1, w+1), dtype=np.float)

threshold = 128

for i in range(h):
    for j in range(w):
        img_dither[i, j] = img_gray_eq[i, j]

for i in range(h):
    for j in range(w):
        old_pix = img_dither[i, j]
        if img_dither[i, j] > threshold:
            new_pix = 255
        else:
            new_pix = 0

        img_dither[i, j] = new_pix

        quant_err = old_pix - new_pix

        if j > 0:
            img_dither[i+1, j-1] = img_dither[i+1, j-1] + quant_err * 3 / 16
        img_dither[i+1, j] = img_dither[i+1, j] + quant_err * 5 / 16
        img_dither[i, j+1] = img_dither[i, j+1] + quant_err * 7 / 16
        img_dither[i+1, j+1] = img_dither[i+1, j+1] + quant_err * 1 / 16

img_dither = img_dither.astype(np.uint8)
img_dither = img_dither[0:h, 0:w]

plt.figure()
plt.imshow(img_dither, vmin=0, vmax=255, cmap=plt.get_cmap("Greys"))

plt.show()
