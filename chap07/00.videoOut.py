#1 카메라 프레임을 동영상 파일로 저장
import cv2, sys
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed"); sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps)
out = cv2.VideoWriter('out.avi', fourcc, fps, (w,h))

if not out.isOpened():
    print('File open failed')
    cap.release(); sys.exit()

while True:
    ret, frame = cap.read()
    if not ret: break;

    out.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(delay) == 27: break
cap.release(); out.release()
cv2.destroyAllWindows()