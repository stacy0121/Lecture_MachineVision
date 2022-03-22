import numpy as np
import cv2

orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0, 0, 0)
image = np.full((300, 500, 3), white, np.uint8)

center = (image.shape[1]//2, image.shape[0]//2)   # 영상 중심 좌표 - 역순 구성 (행렬순에서 역순으로)  *// : 소수점 이하 버림
pt1, pt2 = (300, 50), (100, 220)
shade = (pt2[0] + 2, pt2[1] + 2)                  # 그림자 좌표

cv2.circle(image, center, 100, blue)
cv2.circle(image, pt1, 50, orange, 2)
cv2.circle(image, pt2, 70, cyan, -1)              # 원 내부 채움

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, 'center_blue', center, font, 1.0, blue)
cv2.putText(image, 'pt1_orange', pt1, font, 0.8, orange)
cv2.putText(image, 'pt2.cyan', shade, font, 1.2, black, 2)   # 그림자 효과
cv2.putText(image, 'pt2_cyan', pt2, font, 1.2, cyan, 1)

cv2.imshow("Draw circles", image)
cv2.waitKey(0)