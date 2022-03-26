import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 5, 100, 1)   # pt(지정 좌표)를 클릭 좌표로 변경
        cv2.imshow(title, image)  # 생성하고 영상에 그리기
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x+30, y+30), 100, 2)   # 클릭 좌표에 +30
        cv2.imshow(title, image)

image = np.ones((300, 300), np.uint8) * 255

title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()