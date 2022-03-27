import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), 20, 100)
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x+30, y+30), 100)
        cv2.imshow(title, image)

image = np.full((300, 500), 255, np.uint8)

title = "exercises_11"
cv2.imshow(title, image)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey()
cv2.destroyAllWindows()