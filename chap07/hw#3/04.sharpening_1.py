## 회선이용 샤프닝
import numpy as np, cv2
from Common.filters import filter

image = cv2.imread("dukjo.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (320, 480))
if image is None : raise Exception("영상파일 읽기 오류")

## 샤프닝 마스크 원소 지정
data = [0, -1, 0,
         -1, 5, -1,
         0, -1, 0]
mask = np.array(data, np.float32).reshape(3, 3)   # ndarray 객체 생성 및 형태 변경

sharpen = filter(image, mask)                     # 회선 수행 - 저자 구현 함수
sharpen1 = cv2.convertScaleAbs(sharpen)            # 형변환

cv2.imshow("image", image)
cv2.imshow("sharpen", sharpen1)
cv2.waitKey()