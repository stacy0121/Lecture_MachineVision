import sys, cv2
import numpy as np

# 컬러 영상 영상 불러오기
src = cv2.imread('images_ch06/lenna.bmp')

if src is None:
    print('Image load failed'); sys.exit()

dst = cv2.add(src, 100)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()