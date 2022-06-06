import sys, cv2

src = cv2.imread('images/sheep.jpg')
print(src.shape[:2])

if src is None: print('Image load failed'); sys.exit()

# 5배로 영상 크기 조절(scaling)
dst1 = cv2.resize(src, (0, 0), fx=5, fy=5, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (2400, 1600))
dst3 = cv2.resize(src, (2400, 1600), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (2400, 1600), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1[200:700, 200:700])
cv2.imshow('dst2', dst2[200:700, 200:700])
cv2.imshow('dst3', dst3[200:700, 200:700])
cv2.imshow('dst4', dst4[200:700, 200:700])
cv2.waitKey()