import numpy as np, cv2, sys
import matplotlib.pyplot as plt

src = cv2.imread("chapter7images/campusLibrary2.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

dst1 = cv2.Canny(src, 50, 200)
dst2 = cv2.Canny(src, 120, 200)
dst3 = cv2.Canny(src, 180, 200)   # 엣지 검출
dst3 = cv2.threshold(dst3, 128, 255, cv2.THRESH_BINARY)[1]   # 이진화
data = [[0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]]
mask = np.array(data, np.uint8).reshape(3, 3)
dst3 = cv2.dilate(dst3, mask)   # 팽창
titles = ['src', 'dst1', 'dst2', 'dst3']
images = [src, dst1, dst2, dst3]

plt.figure(figsize=(10,10))
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()