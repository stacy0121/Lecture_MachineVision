import cv2

src = cv2.imread('images_ch05/flowers.jpg', cv2.IMREAD_COLOR)
mask = cv2.imread('images_ch05/maskHeart.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('images_ch05/sunset.jpg', cv2.IMREAD_COLOR)
sh,sw=src.shape[:2]
mh,mw=mask.shape[:2]
dh,dw=dst.shape[:2]
print('src: ',sh,sw,'mask: ',mh,mw,'dst',dh,dw)

dst[mask>0] = src[mask>0]   # boolean 인덱싱

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()