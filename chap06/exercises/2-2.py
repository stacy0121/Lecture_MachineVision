import cv2

image = cv2.imread("hsvColor.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
planes = cv2.split(hsv)
# bgr = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

cv2.imshow("Hue Channel", planes[0])
cv2.imshow("Saturation Channel", planes[1])
cv2.imshow("Value Channel", planes[2])
cv2.waitKey()