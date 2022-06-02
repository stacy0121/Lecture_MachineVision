## 블러링과 캐니 에지를 이용한 컬러 에지 검출
import cv2

def onTrackbar(th):
    rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)
    rep_edge = cv2.Canny(rep_edge, th, th*2, 5)
    h, w = image.shape[:2]
    cv2.rectangle(rep_edge, (0, 0, w, h), 255, -1)
    color_edge = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)
    cv2.imshow("color edge", color_edge)

image = cv2.imread("chapter7images/color_edge.jpg")
if image is None: raise Exception("영상파일 읽기 오류")

th = 50   # 기본값 50
rep_image = cv2.repeat(image, 1, 2)   # 가로 반복 복사
rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("color edge", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Canny th", "color edge", th, 100, onTrackbar)
onTrackbar(th)
cv2.waitKey()