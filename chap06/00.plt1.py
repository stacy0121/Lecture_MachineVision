import cv2
import matplotlib.pyplot as plt
import numpy as np

# 컬러 영상 출력
imgBGR = cv2.imread('images_ch06/lenna.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('images_ch06/lenna.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap ='gray')
plt.show()