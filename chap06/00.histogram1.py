import numpy as np, cv2
import matplotlib.pyplot as plt

src = cv2.imread('images_ch06/lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

plt.subplot(121), plt.axis('off'), plt.imshow(src, cmap='gray')
plt.subplot(122), plt.plot(hist)
plt.show()