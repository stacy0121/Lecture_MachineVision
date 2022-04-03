import numpy as np, cv2
img1 = np.empty((240, 320), dtype=np.uint8)
img2 = np.zeros((240, 320, 3), dtype=np.uint8)
img3 = np.ones((240, 320), dtype=np.uint8) * 255

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('images_ch05/flowers.jpg')
img2 = img1[140:220, 130:250]
img3 = img1[140:220, 130:250].copy()

img2[:,:]=(244,244,0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()