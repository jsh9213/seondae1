import numpy as np

#삼각형의 세 꼭짓점
A = np.array([-1, 2, 0])
B = np.array([2, 1, 3])
C = np.array([1, 1, -1])

#같은 점 A에서 출바라는 두 변의 벡터
u = B - A
v = C - A

#외적 계산
cross_product = np.cross(u, v)

#외적의 길이는 평행사변형의 넓이
parallelogram_area = np.linalg.norm(cross_product)

#삼각형의 넓이는 평행사변형 넓이의 절반
triangle_area = parallelogram_area / 2

print("u = ", u)
print("v = ", v)
print("u x v = ", cross_product)
print(f"평행사변형 넓이: {parallelogram_area:.6f}")
print(f"삼각형 넓이: {triangle_area:.6f}")