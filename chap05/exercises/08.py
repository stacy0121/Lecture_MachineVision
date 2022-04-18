import numpy as np, cv2

image = cv2.imread("images_ch05/color.jpg", cv2.IMREAD_GRAYSCALE       )
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
center = (190, 170)

cv2.ellipse(mask, center, (40, 60), 0, 0, 360, (255,255,255), -1)
dst = cv2.bitwise_and(image, image, mask=mask)   # 관심 영역 복사


cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey()