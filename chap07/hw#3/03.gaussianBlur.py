import numpy as np, cv2, sys

src = cv2.imread('dukjo.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.resize(src, (320, 480))

dstGaussian = cv2.GaussianBlur(src, (0, 0), 3)

cv2.imshow('src', src)
cv2.imshow('dstGaussian', dstGaussian)
cv2.waitKey()