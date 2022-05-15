import sys, cv2
import matplotlib.pyplot as plt

src = cv2.imread('dark1.JPG', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('dark2.JPG', cv2.IMREAD_GRAYSCALE)
src = cv2.resize(src, (360, 240))
shist = cv2.calcHist([src], [0], None, [256], [0, 256])

if src is None:
    print('Image load failed')
    sys.exit()

dst1 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
dst2 = cv2.equalizeHist(src)
dhist1 = cv2.calcHist([dst1], [0], None, [256], [0, 256])
dhist2 = cv2.calcHist([dst2], [0], None, [256], [0, 256])

cv2.imshow("src", src)
cv2.imshow("normalize", dst1)
cv2.imshow("equalize", dst2)
plt.subplot(131), plt.plot(shist)
plt.subplot(132), plt.plot(dhist1)
plt.subplot(133), plt.plot(dhist2)
plt.show()
cv2.waitKey()