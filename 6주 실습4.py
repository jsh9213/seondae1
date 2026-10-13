import numpy as np
np.set_printoptions(precision=2, suppress=True)

#계수 행렬
A = np.array([
    [3, 2, 1],
    [1, 1, 2],
    [2, 1, 1]
], dtype=float)
#상수 벡터 b 
b = np.array([
    [5],
    [1],
    [2]
], dtype=float)

print("계수 행렬 A:")
print(A)
print("\n상수 벡터 b:")
print(b)

#행렬식 계산
det_A = np.linalg.det(A)  #이게 중요함
print("\n행렬식 det(A):")
print(round(det_A, 10))

#역행렬 존재 여부 확인
if np.isclose(det_A, 0):
    print("\ndet(A) = 0이므로 역행렬이 존재하지 않습니다.")
else:
    print("\ndet(A) ≠ 0이므로 역행렬이 존재합니다.")
    #역행렬 계산
    A_inv = np.linalg.inv(A)

    print("\n역행렬 A^(-1):")
    print(A_inv)
    #X = A^(-1) * b
    X = A_inv @ b
    print("\n선형시스템의 해 X:")
    print(X)

    x, y, z = X.flatten()
    print(f"\nx = {x:.0f}")
    print(f"y = {y:.0f}")
    print(f"z = {z:.0f}")

    #검산
    print("\n검산결과: A @ X")
    print(A @ X)