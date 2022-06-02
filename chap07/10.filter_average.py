import numpy as np, cv2

def average_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize//2

    for i in range(center, rows - center):
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            if y1<0 or y2>rows or x1<0 or x2>cols:   # 입력 영상을 벗어나면
                dst[i, j] = image[i, j]              # 필터링 하지 않은 원본 픽셀 배당
            else:
                mask = image[y1:y2, x1:x2]      # 시작위치와 종료위치로 마스크 사각형 선언
                dst[i, j] = cv2.mean(mask)[0]   # (x, 0.0, 0.0, 0.0)
    return dst

image = cv2.imread("chapter7images/filter_avg.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

avg_img = average_filter(image, 5)
blur_img = cv2.blur(image, (5,5), anchor=(-1,-1), borderType=cv2.BORDER_REFLECT)
box_img = cv2.boxFilter(image, ddepth=-1, ksize=(5, 5))

cv2.imshow("image", image)
cv2.imshow("avg_img", avg_img)
cv2.imshow("blur_img", blur_img)
cv2.imshow("box_img", box_img)
cv2.waitKey()