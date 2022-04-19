import cv2

image = cv2.imread("ycrcbColor.jpg")

ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
planes = cv2.split(ycrcb)

cv2.imshow("Y Channel", planes[0])
cv2.imshow("Cr Channel", planes[1])
cv2.imshow("Cb Channel", planes[2])
cv2.waitKey()