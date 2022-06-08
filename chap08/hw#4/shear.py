import sys, cv2, numpy as np

src = cv2.imread("ocean.jpg")   # 563x320
if src is None: print('Image load failed!'); sys.exit()
src = cv2.resize(src, (480, 320))   # resize (INTER_LINEAR)

aff = np.array([[1, 0.3, 0],
                [0, 1, 0]], dtype=np.float32)   # 변환 행렬

h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h*0.3), h))   # affine 변환(shear) + 결과 영상 크기 조정

cv2.imshow('src', src); cv2.imshow('dst', dst)
cv2.waitKey()