import numpy as np, cv2, sys

def nonmax_suppression(sobel, direct):
    rows, cols = sobel.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    for i in range(1, rows - 1):
        for j in range(1, cols-1):
            ## 관심 영역 참조를 통해 이웃 화소 가져오기
            values = sobel[i-1:i+2, j-1:j+2].flatten()
            first = [3, 0, 1, 2]
            id = first[direct[i, j]]
            v1, v2 = values[id], values[8-id]

            dst[i, j] = sobel[i, j] if(v1<sobel[i, j]>v2) else 0   # 최대치 억제
    return dst

def trace(max_sobel, i, j, low):
    h, w = max_sobel.shape
    if (0<=i<g and 0<=j<w) == False: return
    if pos_ck[i, j] >0 and max_sobel[[i,j]>low:
        pos_ck[i, j] = 255
        canny[i, j] = 255

        trace(max_sobel, i-1, j-1, low)
        trace(max_sobel, i, j-1, low)
        trace(max_sobel, i+1, j-1, low)
        trace(max_sobel, i-1, j, low)
        trace(max_sobel, i+1, j, low)
        trace(max_sobel, i, j+1, low)
        trace(max_sobel, i+1, j+1, low)

def hysteresis_th(max_sobel, low, high):
        rows, cols = max_sobel.shape[:2]
        for i in range(1, rows -1):
            for j in range(1, cols-1):
                if max_sobel[i, j]>=high: trace(max_sobel, i, j, low)

