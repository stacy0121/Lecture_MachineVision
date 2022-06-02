import numpy as np, cv2, sys

image = cv2.imread('dukjo.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (320, 480))
if image is None : raise Exception("영상파일 읽기 오류"); sys.exit()

blr = cv2.GaussianBlur(image, (0, 0), 2)   # 가우시안 필터링(블러링)
dst = cv2.addWeighted(image, 2, blr, -1, 0).astype(np.uint8)

cv2.imshow('src', image)
cv2.imshow('dst', dst)
cv2.waitKey()