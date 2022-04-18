import numpy as np, cv2

pts1 = np.array([(200, 50, 1), (400, 50, 1),
                 (400, 250, 1), (200, 250, 1)], np.float32)

theta = 45 * np.pi / 180
m = np.array([[np.cos(theta), -np.sin(theta), 0],
              [np.sin(theta), np.cos(theta), 0],
              [0, 0, 1]], np.float32)

delta = (pts1[2] - pts1[0])//2
center = pts1[0] + delta

## 평행이동 행렬
t1 = np.eye(3, dtype=np.float32)
t2 = np.eye(3, dtype=np.float32)

t1 # 중심좌표 평행이동
t2
## 행렬곱 수행
m2

pts2 = cv2.gemm(pts1, m2, 1, None, 1, flags=cv2.GEMM_2_T)

for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print("pts1[%d] = %s, pst2[%d] = %s" %(i, pt1, i, pt2))

image = np.full((400, 500, 3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1[:, :2])], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(pts2[:, :2])], True, (255, 0, 0), 3)
cv2.imshow("image", image)
cv2.waitKey()