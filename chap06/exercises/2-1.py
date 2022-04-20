## RGB 색상 평면
import cv2

image = cv2.imread("rgbColor.jpg")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   # RGB 색공간을 분리하기 위해 변환
rgb = cv2.split(rgb)                           # RGB 색 평면 분리

cv2.imshow("Blue Channel", rgb[0])    # B
cv2.imshow("Green Channel", rgb[1])   # G
cv2.imshow("Red Channel", rgb[2])     # R
cv2.waitKey()