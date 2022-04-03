import sys, cv2

# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('images_ch05/empireLight.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('images_ch05/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)   # 4채널

if src is None or logo is None:
    print('Image load failed!'); sys.exit()

mask = logo[:,:,3]     # 알파 채널로 만든 마스크 영상
logo = logo[:,:,:-1]   # b,g,r 채널로 구성된 컬러영상
h, w = mask.shape[:2]
crop = src[:h, :w]     # mask와 같은 크기 부분 영상 추출 (슬라이싱)

cv2.copyTo(logo, mask, crop)

cv2.imshow('src',src)
cv2.imshow('logo',logo)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()