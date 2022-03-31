import cv2

col_img = cv2.imread('rgb_small.jpg', cv2.IMREAD_COLOR)
print(col_img.shape)

bgr = cv2.split(col_img)

cv2.imshow("image", col_img)
cv2.imshow("Blue Channel", bgr[0])    # blue 채널
cv2.imshow("Green Channel", bgr[1])   # green 채널
cv2.imshow("Red Channel", bgr[2])     # red 채널
cv2.imshow("Blue Channel+20", bgr[0]+20)   # 넘파이 브로드캐스팅
cv2.imshow("Green Channel+20", bgr[1]+20)
cv2.imshow("Red Channel+20", bgr[2]+20)

cv2.waitKey()
cv2.destroyAllWindows()