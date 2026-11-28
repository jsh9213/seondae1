import numpy as np

# 평행육면체를 이루는 세 벡터
u = np.array([4, 1, 1])
v = np.array([2, 1, 0])
w = np.array([0, 2, 3])

# 1. 외적과 밑면 넓이
cross_product = np.cross(u, v)
S = np.linalg.norm(cross_product)

# 2. 단위 법선벡터와 수직 높이
unit_normal = cross_product / S
h = abs(np.dot(w, unit_normal))

# 3. 밑면 넓이 x 수직 높이
V1 = S * h

# 4. 스칼라 삼중곱의 절댓값
V2 = abs(np.dot(cross_product, w))

# 5. 행렬식의 절댓값으로 검산
A = np.vstack([u, v, w])
V3 = abs(np.linalg.det(A))

print("u x v =", cross_product)
print(f"밑면 넓이 S = {S:.6f}")
print(f"수직 높이 h = {h:.6f}")
print(f"밑면 x 높이로 구한 체적 = {V1:.6f}")
print(f"삼중곱으로 구한 체적 = {V2:.6f}")
print(f"행렬식으로 구한 체적 = {V3:.6f}")