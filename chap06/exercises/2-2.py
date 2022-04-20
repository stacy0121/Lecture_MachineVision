## HSV 색상 평면
import cv2

image = cv2.imread("hsvColor.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)   # HSV 색공간을 분리하기 위해 변환
planes = cv2.split(hsv)                        # 색 평면 분리

cv2.imshow("Hue Channel", planes[0])
cv2.imshow("Saturation Channel", planes[1])
cv2.imshow("Value Channel", planes[2])
cv2.waitKey()