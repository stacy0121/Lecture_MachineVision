import numpy as np, cv2

logo = cv2.imread("images_ch05/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(logo)

empty = np.zeros(logo.shape[:2], np.uint8)   # 빈 채널 생성
blue_img = cv2.merge([blue, empty, empty])   # 채널 합성
green_img = cv2.merge([empty, green, empty])
red_img = cv2.merge([empty, empty, red])

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey()