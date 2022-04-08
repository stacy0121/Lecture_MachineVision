import numpy as np, cv2

image = cv2.imread("exercises/images_ch05/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

min_val, max_val, _, _ = cv2.minMaxLoc(image)   # 최솟값과 최댓값 가져오기

ratio = 255 / (max_val - min_val)
dst = np.round((image-min_val) * ratio).astype('uint8')    # 보정
min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

print("원본 영상 최솟값= %d, 최댓값= %d" %(min_val, max_val))
print("수정 영상 최솟값= %d, 최댓값= %d" %(min_dst, max_dst))
cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey()