import cv2

image = cv2.imread("rgbColor.jpg")

bgr = cv2.split(image)

cv2.imshow("Blue Channel", bgr[0])
cv2.imshow("Green Channel", bgr[1])
cv2.imshow("Red Channel", bgr[2])
cv2.waitKey()