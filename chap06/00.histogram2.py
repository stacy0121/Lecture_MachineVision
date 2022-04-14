import numpy as np, cv2
import matplotlib.pyplot as plt

src = cv2.imread('images_ch06/lenna.bmp')
colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for(p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)
    plt.show()