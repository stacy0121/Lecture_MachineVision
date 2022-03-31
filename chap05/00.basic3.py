import numpy as np, cv2

col_img = cv2.imread('rgb_small.jpg', cv2.IMREAD_COLOR)
h, w = col_img.shape[:2]
add20 = np.zeros((h, w), np.uint8) + 20

bgr = cv2.split(col_img)

cv2.imshow("image", col_img)
cv2.imshow("add20", add20)

cv2.imshow("Blue Channel", bgr[0])
cv2.imshow("Green Channel", bgr[1])
cv2.imshow("Red Channel", bgr[2])

cv2.imshow("Blue Channel add20", cv2.add(bgr[0], add20))   # 최소 0, 최대 255로 제한
cv2.imshow("Green Channel add20", cv2.add(bgr[1], add20))
cv2.imshow("Red Channel add20", cv2.add(bgr[2], add20))

cv2.waitKey()
cv2.destroyAllWindows()