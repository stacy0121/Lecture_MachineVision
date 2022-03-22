import numpy as np
import cv2

def onChange(value):
    global image, title   # 전역 변수 참조

    add_value = value - int(image[0][0])   # 트랙바의 현재값 - 현재 화소값
    print("추가 화소값:", add_value)
    image = image + add_value   # 밝기 변경 - 브로드캐스팅?
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)

title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)   # 트랙바 콜백 함수 등록
cv2.waitKey(0)
cv2.destroyAllWindows()