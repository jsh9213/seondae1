import numpy as np

#입력 벡터: 값을 바꾸어 다른 예제도 계산할 수 있다.
u = np.array([3, -1, 2])
v = np.array([1, -2, 4])

u1, u2, u3 = u
v1, v2, v3 = v

#행렬식 전개 부호: +, -, +
c1 = u2 * v3 - u3 * v2
c2 = -(u1 * v3 - u3 * v1) #가운데 항의 부호 주의
c3 = u1 * v2 - u2 * v1

result = np.array([c1, c2, c3])

print("i 성분:", c1)
print("j 성분:", c2)
print("k 성분:", c3)
print("u x v:", result)

#numpy로 검산
print("Numpy 결과:", np.cross(u, v))

#두 입력 벡터와 수직인지 확인
print("u ' (u x v):", np.dot(u, result))
print("v ' (u x v):", np.dot(v, result))