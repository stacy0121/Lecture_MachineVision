import cv2

image1 = cv2.imread("add1.jpg")
image2 = cv2.imread("add2.jpg")

dst1 = cv2.addWeighted(image1, 1, image2, 0, 0)       # 첫번째 영상 - 1대 0의 비율로 합성
dst2 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)   # 두번째 - 1대 1
dst3 = cv2.addWeighted(image1, 0, image2, 1, 0)       # 세번째 - 0대 1

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey()