import numpy as np, cv2

image = cv2.imread("gelato.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")
image = cv2.resize(image, (380, 380))

## OpenCV 제공 소벨 에지 계산
dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, delta=3)   # x방향 1차 미분 - 수직 마스크
dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)         # y방향 미분
edge2 = cv2.magnitude(dst3, dst4)                                # 벡터 크기 계산
edge2 = np.clip(edge2, 0, 255).astype(np.uint8)                  # saturation

edge3 = np.zeros(image.shape[:2], np.uint8)
edge3[edge2 > 120] = 255                                         # 더 선명하게

cv2.imshow("dst3 - vertical_OpenCV", dst3)
cv2.imshow("dst4 - horizontal_OpenCV", dst4)
cv2.imshow("edge2 - OpenCV", edge2)
cv2.imshow("edge3 - OpenCV", edge3)
cv2.waitKey()