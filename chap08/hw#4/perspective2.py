import numpy as np, cv2, sys

src = cv2.imread("information.jpg")   # 480x360
if src is None: print('Image load failed!'); sys.exit()

height, width = src.shape[:2]

w, h = 480, 320   # 출력이미지 크기

srcQuad = np.array([[47, 56], [396, 53], [420, 279], [5, 271]], np.float32)   # 소스 영상 네 꼭짓점 좌표(왼쪽 위부터 시계방향)
dstQuad = np.array([[0,0], [w-1,0], [w-1,h-1], [0,h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)   # perspective 변환 행렬 반환
dst = cv2.warpPerspective(src, pers, (w, h))           # perspective 변환

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()