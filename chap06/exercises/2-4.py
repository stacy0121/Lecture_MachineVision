import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("dark.JPG")

src = cv2.resize(image, (360, 240))

dst1 = np.clip(src+100., 0, 255).astype(np.uint8)
dst2 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
# bgr_planes = cv2.split(src)
# dst3 = cv2.equalizeHist(src)

hist1 = cv2.calcHist([dst1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([dst2], [0], None, [256], [0, 256])
# hist3 = cv2.calcHist([dst3], [0], None, [256], [0, 256])

plt.plot(hist1)
plt.plot(hist2)
# plt.plot(hist3)
plt.show()