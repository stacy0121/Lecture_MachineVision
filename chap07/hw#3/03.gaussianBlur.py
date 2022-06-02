import cv2

src = cv2.imread('dukjo.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.resize(src, (320, 480))

## 가우시안 필터링
# dstGaussian = cv2.GaussianBlur(src, (0, 0), 3)
dstGaussian = cv2.GaussianBlur(src, (0, 0), 10)   # 시그마 증가

cv2.imshow('src', src)
cv2.imshow('dstGaussian', dstGaussian)
cv2.waitKey()