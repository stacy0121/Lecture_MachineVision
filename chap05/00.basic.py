import sys
import cv2

# 영상 불러오기
gray_img = cv2.imread('rgb_very_small.jpg', cv2.IMREAD_GRAYSCALE)
col_img = cv2.imread('rgb_very_small.jpg', cv2.IMREAD_COLOR)

if gray_img is None or col_img is None:
    print("Image load failed!")
    sys.exit()

# 영상의 속성 참조
print('type(gray_img): ', type(gray_img))   # ndarray
print('gray_img.shape: ', gray_img.shape)   # (11, 14)
print('col_img.shape: ', col_img.shape)     # (11, 14, 3)
print('gray_img.dtype: ', gray_img.dtype)   # uint8

# 영상의 크기 참조
h, w = col_img.shape[:2]
print('col_img size: {} x {}'.format(w, h))

print(gray_img)
print(col_img)

cv2.imshow('gray_img', gray_img)
cv2.imshow('col_img', col_img)
cv2.waitKey()
cv2.destroyAllWindows()