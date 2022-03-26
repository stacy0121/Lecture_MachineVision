import numpy as np, cv2

image = np.full((600, 400, 3), (255, 255, 255), np.uint8)   # 3채널 행렬 생성

cv2.rectangle(image, (100, 100), (300, 400), (0,0,255), -1)

cv2.imshow("exercises_09", image)
cv2.waitKey()
cv2.destroyAllWindows()