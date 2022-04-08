import numpy as np, cv2

img1 = np.empty((120, 160), dtype=np.uint8)
img2 = np.zeros((120, 160, 3), dtype=np.uint8)
img3 = np.ones((120, 160), dtype=np.uint8) * 255

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('exercises/images_ch05/flowers.jpg')
img2 = img1                 # 레퍼런스(참조)
img3 = img2.copy()
img2[:,:,:] = (255,255,0)   # img1에 영향

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()
