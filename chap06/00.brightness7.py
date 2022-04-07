import sys, cv2
import numpy as np

# 컬러 영상 영상 불러오기
src = cv2.imread('images_ch06/lenna.bmp')

if src is None:
    print('Image load failed'); sys.exit()

dst1 = cv2.add(src, (100,100,100,0))
dst2 = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()