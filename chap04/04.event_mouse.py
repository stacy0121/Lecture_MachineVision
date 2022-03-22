import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:   # 마우스 이벤트 종류 사용
        print("마우스 왼쪽 버튼 누르기")
    elif event==cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event==cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event==cv2.EVENT_LBUTTONUP:
        print("마우스 왼쪽 버튼 떼기")

image = np.full((200, 300), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"
cv2.imshow(title1, image)   # 윈도우 생성 및 윈도우 보기
cv2.imshow(title2, image)

cv2.setMouseCallback(title1, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()