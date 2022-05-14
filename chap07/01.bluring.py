## 회선이용 블러링
import numpy as np, cv2

## 회선 수행 함수 - 행렬 처리 방식(속도 면에서 유리)
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)        # 회선 결과 행렬 저장
    ycenter, xcenter = rows//2, cols//2             # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):        # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1   # 관심 영역 높이 범위
            x1, x2 = j - xcenter, j+xcenter+1
            roi = image[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]

    return dst

## 회선 수행 함수 - 화소 직접 근접
def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = rows//2, cols//2

    for i in range(ycenter, rows - ycenter):  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter, j + v - xcenter
                    sum += image[y, x] * mask[u, v]
            dst[i, j] = sum
    return dst

image = cv2.imread("chapter7images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = {1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,}
mask = np.array(data, np.float32).reshape(3,3)
blur1 = filter(image, mask)
blur2 = filter2(image, mask)
blur1 = blur1.astype('uint8')
blur2 = cv2.convertScaleAbs(blur2)   # 윈도우 표시를 위한 형변환

cv2.imshow("image", image)
cv2.imshow("blur1", blur1)
cv2.imshow("blur2", blur2)
cv2.waitKey()