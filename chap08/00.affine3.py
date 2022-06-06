import numpy as np, sys, math, cv2

src = cv2.imread("images/sheep.jpg")

if src is None: print('Image load failed!'); sys.exit()

rad = 45 * math.pi/180   # 45도
aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)   # 45도 회전 변환 행렬

dst = cv2.warpAffine(src, aff, (0, 0))   # affine 변환(Rotation)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey( )