import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안 됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    roi = frame[200:300, 100:300]
    print("관심 영역의 합", cv2.sumElems(roi))                 # (1479792.0, 1454164.0, 1610321.0, 0.0)
    print("관심 영역의 평균(mean() 함수 사용)", cv2.mean(roi))   # (73.98960000000001, 72.7082, 80.51605, 0.0)
    sum, count = 0, 0
    for i in range(roi.shape[0]):
        for j in range(roi.shape[1]):
            sum += roi[i][j]
            count += 1

    print("관심 영역의 평균(원소 순회)", sum/count)

    title = "View Frame from Camera"
    cv2.imshow(title, frame)
capture.release()