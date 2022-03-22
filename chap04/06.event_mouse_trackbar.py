import numpy as np
import cv2

def onChange(value):                      # 트랙바 이벤트 콜백함수
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image = image + add_value
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):   # 마우스 이벤트 콜백함수
    global image, title, bar_name

    if event==cv2.EVENT_RBUTTONDOWN:
        if (image[0][0] < 246): image = image + 10         # +10만큼 밝기 변경(브로드캐스팅)
        cv2.setTrackbarPos(bar_name, title, image[0][0])   # 트랙바 위치도 변경
        cv2.imshow(title, image)

    elif event==cv2.EVENT_LBUTTONDOWN:
        if(image[0][0] >= 10): image -= 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)
title = "Trackbar & Mouse Event"
bar_name = "Brightness"
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()