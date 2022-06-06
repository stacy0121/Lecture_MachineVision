import sys, cv2

src = cv2.imread("images/sheep.jpg")
if src is None: print('Image load failed!'); sys.exit()

cp = (src.shape[1]/2, src.shape[0]/2)   # 중심점

rot = cv2.getRotationMatrix2D(cp, 45, 0.5)   # 중심점 기준 45도 회전, 크기 변환 행렬 반환
dst = cv2.warpAffine(src, rot, (0, 0))       # affine 변환(Rotation)

cv2.imshow('src',src)
cv2.imshow('dst', dst)
cv2.waitKey()