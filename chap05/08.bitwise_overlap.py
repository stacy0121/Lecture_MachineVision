import numpy as np, cv2

image = cv2.imread("exercises/images_ch05/bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("exercises/images_ch05/logo.jpg", cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception("영상파일 읽기 오류")

_, masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)   # 로고 영상 이진화 (첫번째 변수 - boolean)
# masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])   # 전경 통과 마스크
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)        # 배경 통과 마스크

(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W-w)//2, (H-h)//2
roi = image[y:y+h, x:x+w]   # 관심 영역(roi) 지정 (참조)

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)   # 로고의 전경 복사
background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)     # roi에 원본 배경만 복사

dst = cv2.add(background, foreground)   # 로고 전경과 원본 배경 간 합성
image[y:y+h, x:x+w] = dst               # 합성 영상을 원본에 복사

cv2.imshow("image", image)
cv2.waitKey()