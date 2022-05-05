import numpy as np, sys, cv2

src = cv2.imread("chapter7images/flower1.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

kernel = np.ones((5, 5), dtype=np.float64) / 25.
dst = cv2.filter2D(src, -1, kernel)   # -1 : 같은 데이터 타입 영상 출력

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()