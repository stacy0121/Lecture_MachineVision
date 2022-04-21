import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)                        # 255 원소 행렬
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)         # 정규화
    gap = hist_img.shape[1] / hist.shape[0]                         # 한 계급 너비(히스토그램 영상의 열 크기 / 히스토그램 범위)

    for i, h in enumerate(hist):
        x = int(round(i * gap))                                     # 막대 사각형 시작 x 좌표
        w = int(round(gap))                                         # 막대 사각형 가로 길이
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)   # 영상에 막대 사각형 그리기

    return cv2.flip(hist_img, 0)                                    # 영상 x축 대칭

image = cv2.imread("dark.JPG", cv2.IMREAD_GRAYSCALE)

src = cv2.resize(image, (360, 240))                                 # 영상 크기 재조정
dst1 = np.clip(src+30., 0, 255).astype(np.uint8)                    # 명암비 조절
dst2 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)            # 정규화
dst3 = cv2.equalizeHist(src)                                        # 평활화
## 히스토그램 계산
hist1 = cv2.calcHist([dst1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([dst2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([dst3], [0], None, [256], [0, 256])
## 히스토그램 그리기(함수 호출)
hist_img1 = draw_histo(hist1)
hist_img2 = draw_histo(hist2)
hist_img3 = draw_histo(hist3)

cv2.imshow("image1", dst1); cv2.imshow("hist1", hist_img1)          # 영상 처리 후 영상과 히스토그램 출력
cv2.imshow("image2", dst2); cv2.imshow("hist2", hist_img2)
cv2.imshow("image3", dst3); cv2.imshow("hist3", hist_img3)
cv2.waitKey()