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

image = cv2.imread("dark.JPG")                                      # YCrCb로 변환하기 위해 컬러 영상으로 불러옴
src = cv2.resize(image, (360, 240))
src = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)                        # BGR 색공간 영상을 YCrCb 영상으로 변환

## 밝기 정보에 대한 영상 처리
ycrcb_planes = cv2.split(src)
dst1 = cv2.add(ycrcb_planes[0], 30)                                    # 명암비 조절 (saturation 방식)
dst1 = cv2.merge((dst1, ycrcb_planes[1], ycrcb_planes[2]))
dst2 = cv2.normalize(ycrcb_planes[0], None, 0, 200, cv2.NORM_MINMAX)   # 정규화
dst2 = cv2.merge((dst2, ycrcb_planes[1], ycrcb_planes[2]))
dst3 = cv2.equalizeHist(ycrcb_planes[0])                               # 평활화
dst3 = cv2.merge((dst3, ycrcb_planes[1], ycrcb_planes[2]))

## 히스토그램 계산
hist1 = cv2.calcHist([dst1], [0], None, [256], [0, 256])               # 밝기 정보만 계산
hist2 = cv2.calcHist([dst2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([dst3], [0], None, [256], [0, 256])

## 히스토그램 그리기(함수 호출)
hist_img1 = draw_histo(hist1)
hist_img2 = draw_histo(hist2)
hist_img3 = draw_histo(hist3)

dst1 = cv2.cvtColor(dst1, cv2.COLOR_YCrCb2BGR)                         # 영상 출력을 위해 색공간 변환
dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_YCrCb2BGR)

cv2.imshow("image1", dst1); cv2.imshow("hist1", hist_img1)             # 영상 처리 후 영상과 히스토그램 출력
cv2.imshow("image2", dst2); cv2.imshow("hist2", hist_img2)
cv2.imshow("image3", dst3); cv2.imshow("hist3", hist_img3)
cv2.waitKey()