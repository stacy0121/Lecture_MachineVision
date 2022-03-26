import numpy as np, cv2

image = np.full((200, 300), 50, np.uint8)

title1, title2 = "win mode1", "win mode2"

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, 300, 200)
cv2.waitKey()
cv2.destroyAllWindows()