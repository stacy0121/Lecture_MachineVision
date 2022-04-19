import cv2
import numpy as np


def on_trackbar(pos):
    img1 = cv2.getTrackbarPos("image1", "dst")
    img2 = cv2.getTrackbarPos("image2", "dst")

    dst1 = cv2.addWeighted(image1, 1, image2, 0, img1)
    dst2 = cv2.addWeighted(image1, 0.5*img1/50, image2, 0.5*img2/50, 0)
    dst3 = cv2.addWeighted(image1, 0, image2, 1, img2)

    concat = np.concatenate((dst1, dst2, dst3), axis=1)  # 행 방향

    cv2.imshow("dst", concat)

image1 = cv2.imread("add1.jpg")
image2 = cv2.imread("add2.jpg")

dst1 = cv2.addWeighted(image1, 1, image2, 0, 0)
dst2 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
dst3 = cv2.addWeighted(image1, 0, image2, 1, 0)
concat = np.concatenate((dst1, dst2, dst3), axis=1)  # 행 방향
cv2.imshow("dst", concat)

cv2.createTrackbar("image1", "dst", 0, 100, on_trackbar)
cv2.createTrackbar("image2", "dst", 0, 100, on_trackbar)
cv2.waitKey()