import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)   # 0원소 행렬 생성. unsigned int형(8byte)
image[:] = 200                           # 밝은 회색(200) 바탕 영상 생성. 슬라이스 연산자로 행렬 원소값 지정

title1, title2 = 'Position1', 'Position2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)            # flags 매개변수는 자동으로 NORMAL
cv2.moveWindow(title1, 150, 150)   # 가로, 세로
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)   # 행렬 원소를 영상으로 표시
cv2.imshow(title2, image)
cv2.waitKey(0)              # 키 이벤트 대기(무기한)
cv2.destroyAllWindows()     # 열린 모든 윈도우 파괴