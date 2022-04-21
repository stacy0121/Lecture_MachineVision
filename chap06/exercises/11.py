import numpy as np

def calc_histo(image, channels, bsize, ranges):
    shape = bsize if len(channels)>1 else (bsize[0], 1)   # 2채널 이상이면 계급 개수를 shape에 저장하고, 그레이스케일이면 원소 개수 그대로 1행 행렬로 저장
    hist = np.zeros((shape[0], shape[1], len(channels)), np.float32)    # 히스토그램 누적 행렬
    gap = np.divide(ranges[1::2], bsize)                  # 계급 간격 (범위 최댓값/간격수)

    for row in image:                                     # 2차원 행렬 순회 방식
        for val in row:
            idx = np.divide(val, gap).astype('uint8')
            hist[tuple(idx)]+=1
    return hist