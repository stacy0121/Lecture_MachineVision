import numpy as np, cv2      # 이미지(핼렬) 처리와 윈도우 사용을 위해 라이브러리 임포트

image = np.zeros((300, 400), np.uint8)   # uint8형 정수 0으로 이루어진 300행 400열 행렬 생성
image[:] = 100                           # 행렬의 모든 원소를 100으로 변경 (슬라이싱)

title = "exercises_06"                 # 윈도우 이름 변수 생성
cv2.imshow(title, image)              # 윈도우 생성, 행렬을 영상으로 보기
cv2.resizeWindow(title, (600, 500))   # 윈도우의 크기를 (500, 600) 화소로 재조정
# (image의 크기는 변경되지 않는다. 윈도우창을 생성할 때 flags 인수 default값이 cv2.WINDOW_AUTOSIZE라는 것을 이용)

cv2.waitKey(0)             # 키 이벤트가 발생할 때까지 무기한 대기
cv2.destroyAllWindows()    # 모든 윈도우 제거