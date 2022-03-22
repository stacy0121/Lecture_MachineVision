import numpy as np
import cv2

switch_case = {ord('a'):"a키 입력",          # ord() 함수: 문자 -> 아스키코드 변환
               ord('b'):"b키 입력",
               0x41:"A키 입력",
               int('0x42', 16):"B키 입력",   # 0x42(16진수) -> 10진수 변환
               2424832:"왼쪽 화살표키 입력",
               2490368:"윗쪽 화살표키 입력",
               2555904:"오른쪽 화살표키 입력",
               2621440:"아래쪽 화살표키 입력"}

image = np.ones((200, 300), np.float)   # image.fill(255)와 같다
cv2.namedWindow('Keyboard Event')
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100)        # 키에 대한 아스키코드 반환
    if key == 27: break             # ESC 키를 누르면 종료

    try :
        result = switch_case[key]   # value 반환
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()