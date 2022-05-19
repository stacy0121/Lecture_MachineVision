import sys, cv2

# green screen mp4 file
cap1 = cv2.VideoCapture('me.mp4')

if not cap1.isOpened():
    print('video open failed')
    sys.exit()

cap2 = cv2.VideoCapture('ocean.mp4')

if not cap2.isOpened():
    print('video open failed')
    sys.exit()

# check the size - cap1 동영상 WIDTH, HEIGHT
w1 = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h1 = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('** foreground', '-'*15)
print('width x height: {} x {}'.format(w1, h1))
print('** background', '-'*15)

# check the size - cap2 동영상 WIDTH, HEIGHT
w2 = round(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
h2 = round(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('width x height: {} x {}'.format(w2, h2))
print('-'*30)

# frame_cap1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
# frame_cap2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
# print('frame_cap1: ', frame_cap1)
# print('frame_cap2: ', frame_cap2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

# composite flag
compositFlag = False

## 동영상 파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("chormaKey.avi", cv2.VideoWriter_fourcc(*'DIVX'), fps, (1280, 720))

while True:
    ret1, frame1 = cap1.read()
    if not ret1: break

    # composit if compositFlag is True
    if compositFlag:
        ret2, frame2 = cap2.read()
        if not ret2: break
        frame2 = cv2.resize(frame2, (1280, 720))

        # composite in HSV color table selected
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        # mask = cv2.inRange(hsv, (50, 150, 0), (150, 255, 255))
        mask = cv2.inRange(hsv, (50,120,0), (70,255,255))   # 머리카락...
        cv2.copyTo(frame2, mask, frame1)   # frame1에 저장

    writer.write(frame1)
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # if you press spacebar, toggle compositFlag
    if key == ord(' '):
        compositFlag = not compositFlag
    elif key == 27: break

cap1.release()
cap2.release()
cv2.destroyAllWindows()