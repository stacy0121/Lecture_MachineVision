import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), radius, 100, thick)   # radius, thick 변수로 대체
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x+30, y+30), 100, thick)   # thick
        cv2.imshow(title, image)

def onChangeT(value):   # 선 두께에 대한 트랙바 이벤트 콜백함수 정의
    global thick        # thick을 전역변수로 선언
    add_thick = value - thick
    thick += add_thick
    cv2.imshow(title, image)

def onChangeR(value):   # 원 반지름에 대한 트랙바 이벤트 콜백함수 정의
    global radius       # radius를 전역변수로 선언
    add_radius = value - radius
    radius += add_radius
    cv2.imshow(title, image)

image = np.full((300, 500), 255, np.uint8)

thick, radius = 1, 20   # 변수 초기화
title = "exercises_11"
cv2.imshow(title, image)

## 트랙바 생성 및 각각의 콜백 함수 등록
cv2.createTrackbar("Thickness", title, thick, 10, onChangeT)   # 두께의 변화를 위해 value 자리에 thick 변수를 넣음.
cv2.createTrackbar("Radius", title, radius, 50, onChangeR)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey()
cv2.destroyAllWindows()