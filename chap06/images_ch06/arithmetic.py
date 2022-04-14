import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src1 = cv2.imread('openCVhistoEq.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('userHistoEq.jpg', cv2.IMREAD_GRAYSCALE)
print("h1 w1",src1.shape[:2])
print("h2 w2",src2.shape[:2])

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

plt.subplot(141), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(142), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(143), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(144), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()
