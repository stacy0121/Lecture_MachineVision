import cv2

# 영상 불러오기
col_img = cv2.imread('rgb_small.jpg', cv2.IMREAD_COLOR)
print(col_img.shape)

bgr = cv2.split(col_img)   # 채널 분리: 컬러영상 -> 3채널 분리 (리스트 반환)
# blue, green, red = cv2.split(col_img)

# 각 채널을 윈도우에 띄우기
cv2.imshow("image", col_img)
cv2.imshow("Blue Channel", bgr[0])    # blue 채널 (Brightness)
cv2.imshow("Green Channel", bgr[1])   # green 채널
cv2.imshow("Red Channel", bgr[2])     # red 채널

cv2.waitKey()
cv2.destroyAllWindows()