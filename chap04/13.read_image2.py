import cv2
from Common.utils import print_matInfo

title1, title2 = 'color2gray', 'color2color'
color2gray = cv2.imread("ch04_images/read_color.jpg", cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("ch04_images/read_color.jpg", cv2.IMREAD_COLOR)
if color2gray is None or color2color is None:
    raise Exception

print("행렬 좌표(100, 100) 화소값")
print("%s %s" % (title1, color2gray[100, 100]))
print("%s %s" % (title2, color2color[100, 100]))

print_matInfo(title1, color2gray)
print_matInfo(title2, color2color)
cv2.imshow(title1, color2gray)
cv2.imshow(title2, color2color)
cv2.waitKey()