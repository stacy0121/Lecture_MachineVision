import numpy as np, cv2
from Common.filters import differential

image = cv2.imread("gelato.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")
image = cv2.resize(image, (380, 380))

data1 = [-1, 0, 1,     # 수직 소벨 마스크
        -2, 0, 2,
        -1, 0, 1]
data2 = [-1, -2, -1,   # 수평 소벨 마스크
         0, 0, 0,
         1, 2, 1]
## 사용자 정의 함수(엣지 검출)
edge1, dst1, dst2 = differential(image, data1, data2)

cv2.imshow("dst1 - vertical_mask", dst1)
cv2.imshow("dst2 - horizontal_mask", dst2)
cv2.imshow("edge1 - User", edge1)
cv2.waitKey()