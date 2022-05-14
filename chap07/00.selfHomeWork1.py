import numpy as np, cv2
src = cv2.imread("chapter7images/pinkRose.png")

if src is None: raise Exception("영상파일 읽기 오류")

# Median Blurring
dst = cv2.blur(src, (3, 3))
# Gaussian Blurring
dst1 = cv2.GaussianBlur(src, (0, 0), 2)   # 커널 크기 자동 지정
# Sharpening
dst2 = cv2.addWeighted(src, 2, dst1, -1, 0).astype(np.uint8)
#dst2 = np.clip(2.0*src - dst1, 0, 255).astype(np.uint8)

cv2.imwrite("mBlur.png", dst)
cv2.imwrite("gBlur.png", dst1)
cv2.imwrite("edgeMov.png", dst2)
cv2.waitKey()
cv2.destroyAllWindows()