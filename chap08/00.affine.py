import numpy as np, cv2, sys

src = cv2.imread('images/sheep.jpg')
if src is None:
    print('Image load failed'); sys.exit()

aff = np.array([[1, 0, 100],
               [0, 1, 50]], dtype=np.float32)   # 변환 행렬

dst = cv2.warpAffine(src, aff, (0, 0))   # affine 변환(Translation)

cv2.imshow('src', src); cv2.imshow('dst', dst)
cv2.waitKey()