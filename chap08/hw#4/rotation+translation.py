import math
import sys, cv2, numpy as np

src = cv2.imread("fire.jpg")   # 320x320
if src is None: print('Image load failed!'); sys.exit()

# rotation
rad = 7 * math.pi/180   # 7도
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)   # 반시계방향 7도 회전 변환 헹렬
dst = cv2.warpAffine(src, aff, (0, 0))   # affine 변환

# Translation
aff2 = np.array([[1, 0, src.shape[1]/5],
                [0, 1, 0]], dtype=np.float32)   # x축 이동 변환 행렬
dst2 = cv2.warpAffine(dst, aff2, (480, 320))      # affine 변환 + 영상 크기 조정(좌우 늘리기)

cv2.imshow('src', src)
cv2.imshow('rotation+translation', dst2)
cv2.waitKey()