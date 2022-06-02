## 모폴로지 침식 연산
import numpy as np, cv2

def erode(img, mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8)

    # xcenter, ycenter = int(mask.shape[1]/2), int(mask.shape[0]/2)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]   # 마스크 중심 좌표

    mcnt = cv2.countNonZero(mask)
    for i in range(ycenter, img.shape[0] - ycenter):
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i+ycenter+1
            x1, x2 = j - xcenter, j+xcenter+1
            roi = img[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)
            dst[i, j] = 255 if (cnt==mcnt) else 0
    return dst

image = cv2.imread("chapter7images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [0, 1, 0,
        1, 1, 1,
        0, 1, 0]
mask = np.array(data, np.uint8).reshape(3, 3)
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]   # 이진화된 이미지 반환

dst1 = erode(th_img, mask)       # 사용자 정의 침식 함수
dst2 = cv2.erode(th_img, mask)   # OpenCV의 침식 함수
# dst2 = cv2.morphologyEx(th_img, cv2.MORPH_ERODE, mask)

cv2.imshow("image", image)
cv2.imshow("binary image", th_img)
cv2.imshow("User erode", dst1)
cv2.imshow("OpenCV erode", dst2)
cv2.waitKey()