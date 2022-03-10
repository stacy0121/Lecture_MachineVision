import numpy as np
import cv2

image = np.zeros((300, 400), np.uint8)   # grayscale. 1Byte 사용
image.fill(200)

cv2.imshow("Window title", image)
cv2.waitKey(0)   # 클릭했을 때
cv2.destroyAllWindows()