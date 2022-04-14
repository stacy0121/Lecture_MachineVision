import sys, cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('images_ch06/grayCity.jpg', cv2.IMREAD_GRAYSCALE)
shist = cv2.calcHist([src], [0], None, [256], [0, 256])

if src is None:
    print('Image load failed')
    sys.exit()

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
dhist = cv2.calcHist([dst], [0], None, [256], [0, 256])

plt.subplot(121), plt.plot(shist)
plt.subplot(122), plt.plot(dhist)
plt.show()