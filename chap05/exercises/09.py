import numpy as np, cv2

m = np.empty((3, 6), dtype=np.uint8)

reduce_avg1 = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_AVG)   # 열방향 축소
reduce_avg2 = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG)   # 행방향 축소

print("가로 방향 평균", reduce_avg1)
print("세로 방향 평균", reduce_avg2)