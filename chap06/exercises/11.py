import numpy as np


def calc_histo(image, channels, bsize, ranges):
    shape = bsize if len(channels)>1 else (bsize[0], 1)   # 채널이 1개 이상이면 계급 단위 자체를 shape에 저장하고, 아니면 원소 1을 추가해서 튜플로 저장
    hist = np.zeros((shape[:2], channels), np.float32)    # 히스토그램 누적 행렬
    gap = np.divide((ranges[1::2], bins)                  # 계급 간격 (나눗셈)

    for row in image:                                     # 2차원 행렬 순회 방식
        for val in row:
            idx = np.divide(val[channels], gap).astype('uint')
            hist[tuple(idx)]+=1
    return hist
