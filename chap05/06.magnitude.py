import numpy as np, cv2

x = np.array([1, 2, 3, 5, 10], np.float32)
y = np.array([2, 5, 7, 2, 9]).astype("float32")

mag = cv2.magnitude(x, y)                # 크기 계산
ang = cv2.phase(x, y)                    # 각도(방향) 계산
p_mag, p_ang = cv2.cartToPolar(x, y)     # 크기와 각도
x2, y2 = cv2.polarToCart(p_mag, p_ang)   # 직교좌표로 변환

print("[x] 형태: %s 원소: %s" % (x.shape, x))         # 1차원 행렬
print("[mag] 형태: %s 원소: \n%s" % (mag.shape, mag))   # 2차원 열벡터

print(">>>열벡터를 1행에 출력하는 방법")
print("[m_mag] = %s" % mag.T)
print("[p_mag] = %s" % np.ravel(p_mag))   # 전개
print("[p_ang] = %s" % np.ravel(p_ang))
print("[x_mat2] = %s" % x2.flatten())     # 전개
print("[y_mat2] = %s" % y2.flatten())