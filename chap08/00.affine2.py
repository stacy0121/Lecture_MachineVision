import numpy as np, cv2, sys

src = cv2.imread('images/sheep.jpg')
if src is None:
    print('Image load failed'); sys.exit()

aff = np.array([[1, 0.5, 0],
               [0, 1, 0]], dtype=np.float32)   # 변환 행렬

h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h*0.5), h))   # affine 변환(Shear)

cv2.imshow('src', src); cv2.imshow('dst', dst)
cv2.waitKey()