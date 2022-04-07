import sys, cv2
import numpy as np

src = cv2.imread('images_ch06/hydrangea.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!'); sys.exit()

dst1 = cv2.add(src, 50, dtype=cv2.CV_8U)
dst2 = cv2.add(src, -50, dtype=cv2.CV_8U)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()