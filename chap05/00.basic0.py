import cv2

gray_img = cv2.imread('rgb_small.jpg', cv2.IMREAD_GRAYSCALE)
col_img = cv2.imread('rgb_small.jpg', cv2.IMREAD_COLOR)

print('type(gray_img): ', type(gray_img))
print('gray_img.shape: ', gray_img.shape)
print('col_img.shape: ', col_img.shape)
print('gray_img.dtype: ', gray_img.dtype)
print('-'*20)
print(gray_img[:3, :3])
print('-'*20)
print(col_img[:3, :3])
print('-'*20)

# 영상의 크기 참조
h, w = col_img.shape[:2]
print('col_img size: {} x {}'.format(w, h))

if len(gray_img.shape) == 2: print('gray_img is a grayscale image')
elif len(gray_img.shape) == 3: print('gray_img is a truecolor image')
cv2.imshow('gray', gray_img)
cv2.imshow('color', col_img)
cv2.waitKey()
cv2.destroyAllWindows()