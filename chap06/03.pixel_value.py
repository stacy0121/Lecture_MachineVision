## 영상 화소값 확인
import cv2

image = cv2.imread("images_ch06/dolls.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

(x, y), (h, w) = (180, 37), (15, 10)   # 좌표는 x, y
roi_img = image[y:y+h, x:x+w]          # 행렬 접근은 y, x

print("[roi_img] =")
for row in roi_img:
    for p in row:
        print("%4d" %p, end=" ")
print()

cv2.rectangle(image, (x, y, w, h), 255, 1)
cv2.imshow("image", image)
cv2.waitKey()