import sys, cv2

def onTrackbar(th):
    rot = cv2.getRotationMatrix2D(cp, th, 1 - th/360)  # 중심점 기준 회전, 크기 변환 행렬 반환
    dst = cv2.warpAffine(src, rot, (0, 0))  # affine 변환(Rotation)
    cv2.imshow('scaling_effects', dst)

src = cv2.imread("ocean.jpg")
if src is None: print('Image load failed!'); sys.exit()
src = cv2.resize(src, (480, 320))   # resize (INTER_LINEAR)

th = 0
cp = (src.shape[1]/2, src.shape[0]/2)   # 중심점

cv2.namedWindow('scaling_effects')
cv2.createTrackbar('scale', 'scaling_effects', th, 360, onTrackbar)
onTrackbar(th)
cv2.waitKey()