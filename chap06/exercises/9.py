import numpy as np, cv2

def on_trackbar(pos):
    img1 = cv2.getTrackbarPos("image1", "dst")   # 트랙바가 2개이므로 각각의 현재값을 가져옴
    img2 = cv2.getTrackbarPos("image2", "dst")

    dst1 = cv2.addWeighted(image1, 1, image2, 0, img1)                    # 첫번째 - img1만큼 image1의 밝기 변경
    dst2 = cv2.addWeighted(image1, 0.5*img1/50, image2, 0.5*img2/50, 0)   # 두번째 - 각각의 현재값에 따라 밝기 조정 
    dst3 = cv2.addWeighted(image1, 0, image2, 1, img2)                    # 세번째 - img2만큼 imag2의 밝기 변경

    concat = np.concatenate((dst1, dst2, dst3), axis=1)                   # 행 방향으로 붙이기

    cv2.imshow("dst", concat)

image1 = cv2.imread("add1.jpg")
image2 = cv2.imread("add2.jpg")

dst1 = cv2.addWeighted(image1, 1, image2, 0, 0)        # 첫번째 영상 - 1대 0의 비율로 합성
dst2 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)    # 두번째 - 1대 1
dst3 = cv2.addWeighted(image1, 0, image2, 1, 0)        # 세번째 - 0대 1
concat = np.concatenate((dst1, dst2, dst3), axis=1)    # 행 방향으로 붙이기
cv2.imshow("dst", concat)

## image1과 image2의 합성 비율을 각각 조정하는 트랙바 2개
cv2.createTrackbar("image1", "dst", 0, 100, on_trackbar)   # 0에서 시작, 최댓값 100
cv2.createTrackbar("image2", "dst", 0, 100, on_trackbar)
cv2.waitKey()