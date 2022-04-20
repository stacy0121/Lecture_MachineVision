## YCrCb 색상 평면
import cv2

image = cv2.imread("ycrcbColor.jpg")

ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)   # YCrCb 색공간을 분리하기 위해 변환
planes = cv2.split(ycrcb)                          # 색 평면 분리

cv2.imshow("Y Channel", planes[0])
cv2.imshow("Cr Channel", planes[1])
cv2.imshow("Cb Channel", planes[2])
cv2.waitKey()