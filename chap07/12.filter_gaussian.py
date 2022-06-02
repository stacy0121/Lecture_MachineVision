# 가우시안 스무딩 필터링
import numpy as np, cv2

def getGaussianMask(ksize, sigmaX, sigmaY):
    sigma = 0.3 * ((np.array(ksize) - 1.0) * 0.5 - 1.0) + 0.8   # [2.9 1.1]
    if sigmaX <= 0: sigmaX = sigma[0]   # 표준편차가 양수 아닐 때
    if sigmaY <= 0: sigmaY = sigma[1]   # ksize로 기본 표준편차 계산
    
    u = np.array(ksize)//2
    x = np.arange(-u[0], u[0]+1, 1)   # x 방향 범위
    y = np.arange(-u[1], u[1]+1, 1)
    x, y = np.meshgrid(x, y)          # 정방 행렬 생성
    
    ratio = 1/(sigmaX*sigmaX*2*np.pi)
    v1 = x**2/(2*sigmaX**2)
    v2 = y**2/(2*sigmaY**2)
    mask = ratio * np.exp(-(v1+v2))   # 2차원 정규분포 수식
    return mask/np.sum(mask)        # 원소 전체 합 1 유지

image = cv2.imread("chapter7images/smoothing.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

ksize = (17, 5)
gaussian_2d = getGaussianMask(ksize, 0, 0)                      # 2차원 가우시안 마스크 생성
gaussian_1dX = cv2.getGaussianKernel(ksize[0], 0, cv2.CV_32F)   # 1차원 가우시안 마스크 생성 - x 방향
gaussian_1dY = cv2.getGaussianKernel(ksize[1], 0, cv2.CV_32F)   # y 방향

gauss_img1 = cv2.filter2D(image, -1, gaussian_2d)                     # 사용자 생성 마스크 적용
gauss_img2 = cv2.GaussianBlur(image, ksize, 0)
gauss_img3 = cv2.sepFilter2D(image, -1, gaussian_1dX, gaussian_1dY)   # 1차원 가우시안 마스크 적용

titles = ['image', 'gauss_img1', 'gauss_img2', 'gauss_img3']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey()