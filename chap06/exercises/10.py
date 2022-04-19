## 명암도 영상 생성
import numpy as np, cv2

image = np.full((50, 512), 0.7, np.float32)
rows, cols = image.shape[:2]

for i in range(rows):                      # 행렬 전체 조회
    for j in range(cols):                  # 0~512
        image.itemset((i, j), 0.7-(j/cols))         # 화소값 점진적 감소

cv2.imshow("image", image)
cv2.waitKey()