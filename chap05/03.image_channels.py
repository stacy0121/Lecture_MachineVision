import cv2

image = cv2.imread("images_ch05/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")
if image.ndim != 3: raise Exception("컬러 영상 아님")

bgr = cv2.split(image)
print("bgr 자료형: ", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소 개수: ", len(bgr))

## 각 채널을 윈도우에 띄우기
cv2.imshow("image", image)
cv2.imshow("Blue Channel", bgr[0])    # blue 채널
cv2.imshow("Green Channel", bgr[1])   # green 채널
cv2.imshow("Red Channel", bgr[2])     # red 채널
# cv2.imshow("Blue Channel", image[:,:,0])    # 1차원
# cv2.imshow("Green Channel", image[:,:,1])   # 2차원
# cv2.imshow("Red Channel", image[:,:,2])     # 3차원
cv2.waitKey()
cv2.destroyAllWindows()