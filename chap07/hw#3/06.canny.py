import cv2, sys

cap = cv2.VideoCapture('chromaKey.avi')
if not cap.isOpened():
    print('video open failed')
    sys.exit()

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

## 동영상 파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("canny_openCV.mp4", cv2.VideoWriter_fourcc(*'MP4V'), fps, (1280, 720), False)

while True:
    ret1, frame1 = cap.read()
    if not ret1: break
    frame1 = cv2.resize(frame1, (1280, 720))

    ## 캐니 엣지 검출
    # dst = cv2.Canny(frame1, 50, 150)
    dst = cv2.Canny(frame1, 190, 200)    # threshold 조정

    writer.write(dst)                    # 엣지 검출된 프레임 저장
    cv2.imshow('frame', dst)
    key = cv2.waitKey(delay)

    if key == 27: break

cap.release()
cv2.destroyAllWindows()