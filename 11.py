import numpy as np
import matplotlib.pyplot as plt


cX, cY = -0.7, 0.27015
moveX, moveY = 0.0, 0.0
maxIter = 255
image = np.zeros((200, 200))
ppoints, qpoints = 200, 200

for x in range(ppoints):
    for y in range(qpoints):
        zx = 1.5 * (x - ppoints / 2) / (0.5 * 1 * ppoints) + moveX
        zy = 1.0 * (y - qpoints / 2) / (0.5 * 1 * qpoints) + moveY
        i = maxIter
        while zx * zx + zy * zy < 4 and i > 1:
            tmp = zx * zx - zy * zy + cX
            zy, zx = 2.0 * zx * zy + cY, tmp
            i -= 1

        image[x, y] = i

plt.imshow(-image.T, cmap='Greys')
plt.show()