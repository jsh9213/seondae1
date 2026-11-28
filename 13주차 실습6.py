import numpy as np

u = np.array([2, -5, -1])
v = np.array([3, 2, -3])

# 1. 같은 성분끼리 곱한 뒤 더하기
products = u * v
dot_manual = np.sum(products)

# 2. NumPy 함수로 내적 계산
dot_uv = np.dot(u, v)
dot_vu = np.dot(v, u)

# 3. 열벡터의 전치와 행렬 곱으로 계산
u_col = u.reshape(3, 1)
v_col = v.reshape(3, 1)

dot_matrix = (u_col.T @ v_col).item()

print("성분별 곱 =", products)
print("성분별 곱의 합 =", dot_manual)
print("u · v =", dot_uv)
print("v · u =", dot_vu)
print("u^T v =", dot_matrix)
print("교환법칙 확인:", bool(dot_uv == dot_vu))