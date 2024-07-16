N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 各値の絶対値の差の総和を計算して最小の変換回数を求める
sum_diff = 0
for i in range(N):
    sum_diff += abs(A[i] - B[i])

if sum_diff > K:
    print('No')
    exit()

# 偶奇が同じかチェック
if sum_diff % 2 == 0 and K % 2 == 0:
    print('Yes')
elif sum_diff % 2 != 0 and K % 2 != 0:
    print('Yes')
else:
    print('No')