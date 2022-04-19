import cv2

# 마스크 영상을 이용한 영상 합성
src = cv2.imread('exercises/images_ch05/flowers.jpg', cv2.IMREAD_COLOR)
mask = cv2.imread('exercises/images_ch05/maskHeart.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('exercises/images_ch05/sunset.jpg', cv2.IMREAD_COLOR)
sh,sw=src.shape[:2]
mh,mw=mask.shape[:2]
dh,dw=dst.shape[:2]
print('src: ',sh,sw,'mask: ',mh,mw,'dst',dh,dw)

cv2.copyTo(src, mask, dst)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()