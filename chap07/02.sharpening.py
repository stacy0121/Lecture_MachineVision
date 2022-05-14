## 회선이용 샤프닝
import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("chapter7images/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")

## 샤프닝 마스크 원소 지정
data1 = [0, -1, 0,
         -1, 5, -1,
         0, -1, 0]
data2 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]
mask1 = np.array(data1, np.float32).reshape(3, 3)   # ndarray 객체 생성 및 형태 변경
mask2 = np.array(data2, np.float32)

sharpen1 = filter(image, mask1)                     # 회선 수행 - 저자 구현 함수
sharpen2 = filter(image, mask2)
sharpen1 = cv2.convertScaleAbs(sharpen1)            # 형변환
sharpen2 = cv2.convertScaleAbs(sharpen2)

cv2.imshow("image", image)
cv2.imshow("sharpen1", sharpen1)
cv2.imshow("sharpen2", sharpen2)
cv2.waitKey()