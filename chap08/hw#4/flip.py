import sys, cv2, numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("ocean.jpg")
if src is None: print('Image load failed!'); sys.exit()
dst = cv2.resize(src, (480, 320))   # resize (INTER_LINEAR)

# 수평 맞추기
cp = (src.shape[1]/2, src.shape[0]/2)         # 중심점
rot = cv2.getRotationMatrix2D(cp, -1, 1.1)    # 중심점 기준 시계 방향으로 1도 회전, 크기 변환 행렬 반환
dst = cv2.warpAffine(src, rot, (0, 0))        # affine 변환(Rotation)
dstRGB = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)   # opencv 컬러 공간: RGB

# 대칭 이동
flip = np.flip(dst, 1)   # y축 대칭
flipRGB = cv2.cvtColor(flip, cv2.COLOR_BGR2RGB)

plt.subplot(121); plt.axis('off'); plt.imshow(flipRGB)   # 대칭 이동한 영상
plt.subplot(122); plt.axis('off'); plt.imshow(dstRGB)    # 원본 영상
plt.show()