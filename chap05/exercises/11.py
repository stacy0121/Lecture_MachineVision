import numpy as np, cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안 됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    mask = np.zeros(frame.shape, np.uint8)   # (480, 640, 3)
    mask[30:270, 30:350, :] = (1, 1, 1)
    #image = cv2.bitwise_and(frame, frame, mask=mask)
    image = cv2.copyTo(frame, mask)
    cv2.rectangle(image, (30, 30, 320, 240), (0, 0, 255), 3)

    title = "main window"
    cv2.imshow(title, image)
    cv2.resizeWindow(title, 400, 300)
capture.release()