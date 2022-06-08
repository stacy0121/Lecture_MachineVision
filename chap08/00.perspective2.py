# 투시 변환으로 비뚤어진 문서 펴기
import numpy as np, cv2, sys

def drawROI(img, corners):   # call by reference
    cpy = img.copy()

    c1 = (192, 192, 255)   # color
    c2 = (128, 128, 255)

    for pt in corners:
        cv2.circle(cpy, tuple(pt.astype(int)), 25, c1, -1, cv2.LINE_AA)   # UI

    cv2.line(cpy, tuple(corners[0].astype(int)), tuple(corners[1].astype(int)), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1].astype(int)), tuple(corners[2].astype(int)), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2].astype(int)), tuple(corners[3].astype(int)), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3].astype(int)), tuple(corners[0].astype(int)), c2, 2, cv2.LINE_AA)
    
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)   # 원본 영상과 복사본을 합침
    
    return disp

def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(srcQuad[i] - (x, y)) < 25:   # 마우스 좌표가 어떤 원 안에 있을 때
                dragSrc[i] = True
                ptOld = (x, y)
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:          # 움직이는 원
                dx = x - ptOld[0]   # 현재 좌표 - 최초 눌렀을 때 x좌표
                dy = y - ptOld[1]

                srcQuad[i] += (dx, dy)        # 좌표 이동

                cpy = drawROI(src, srcQuad)   # UI 이동
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break

src = cv2.imread('images/matisse.jpg')
if src is None: print('Image load failed!'); sys.exit()

h, w = src.shape[:2]
print("src", w, h)   # 가로, 세로 크기 출력

dw = 500
dh = round(dw * 297/210)   # A4 용지 크기: 210x297cm

# 모서리 점들의 좌표, 드래그 상태 여부
srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)   # 처음 위치
dstQuad = np.array([[0, 0], [0, dh-1], [dw-1, dh-1], [dw-1, 0]], np.float32)
dragSrc = [False, False, False, False]

# 모서리짐, 사각형 그리기
disp = drawROI(src, srcQuad)   # 영상 반환

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13:   # ENTER 키
        break
    elif key == 27:   # ESC 키
        cv2.destroyAllWindows('img')
        sys.exit()

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)
cv2.imshow('dst', dst)
cv2.waitKey()