import numpy as np, cv2

image = cv2.imread("images_ch05/sunset.jpg", cv2.IMREAD_GRAYSCALE)   # (535, 801, 3)

roi1 = image[200:400, 100:400]   # 참조
roi2 = image[300:500, 400:600]

image[200:400, 100:400] = cv2.add(roi1, 50)

min_val, max_val, _, _ = cv2.minMaxLoc(roi2)
ratio = 255 / (max_val - min_val)   # 정규화
image[300:500, 400:600] = np.round((roi2 - min_val) * ratio).astype('uint8')

cv2.imshow("main window", image)
cv2.waitKey()