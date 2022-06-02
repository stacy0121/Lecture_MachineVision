import cv2, sys
import matplotlib.pyplot as plt

src = cv2.imread("chapter7images/campusLibrary2.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

dst1 = cv2.Canny(src, 50, 200)
dst2 = cv2.Canny(src, 120, 200)
dst3 = cv2.Canny(src, 180, 200)
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