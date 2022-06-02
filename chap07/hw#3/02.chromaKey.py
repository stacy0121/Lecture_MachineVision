# import sys, cv2
#
# # green screen mp4 file
# cap1 = cv2.VideoCapture('me.mp4')
# if not cap1.isOpened():
#     print('video open failed')
#     sys.exit()
#
# cap2 = cv2.VideoCapture('ocean.mp4')
# if not cap2.isOpened():
#     print('video open failed')
#     sys.exit()
#
# fps = cap1.get(cv2.CAP_PROP_FPS)
# delay = int(1000/fps)
#
# # composite flag
# compositFlag = False
#
# ## 동영상 파일 개방 및 코덱, 해상도 설정
# writer = cv2.VideoWriter("chromaKey.avi", cv2.VideoWriter_fourcc(*'DIVX'), fps, (1280, 720))
#
# while True:
#     ret1, frame1 = cap1.read()
#     if not ret1: break
#
#     if compositFlag:
#         ret2, frame2 = cap2.read()
#         if not ret2: break
#         frame2 = cv2.resize(frame2, (1280, 720))
#
#         hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)       # 크로마키 추출을 위해 HSV로 변환
#         # mask = cv2.inRange(hsv, (50, 150, 0), (150, 255, 255))
#         mask = cv2.inRange(hsv, (50,120,0), (70,255,255))   # 특정 범위 원소 추출
#         cv2.copyTo(frame2, mask, frame1)                    # 추출한 부분에 한하여 frame2를 frame1에 합성
#
#     writer.write(frame1)
#     cv2.imshow('frame', frame1)
#     key = cv2.waitKey(delay)
#
#     # if you press spacebar, toggle compositFlag
#     if key == ord(' '):
#         compositFlag = not compositFlag
#     elif key == 27: break
#
# cap1.release()
# cap2.release()
# cv2.destroyAllWindows()