N = int(input())
B = list(map(int, input().split()))

# Aの初期化
A = [0] * N

# Aの各要素に対する最大値を計算
A[0] = B[0]
A[N-1] = B[N-2]
for i in range(1, N-1):
    A[i] = min(B[i-1], B[i])

# Aの要素の総和を計算
print(sum(A))