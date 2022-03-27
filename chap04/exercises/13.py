import cv2

image = cv2.imread("read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 100)
params_png = [cv2.IMWRITE_PNG_COMPRESSION]

cv2.imwrite("test.jpg", image, params_jpg)
cv2.imwrite("test.png", image, params_png)
print("저장 완료")