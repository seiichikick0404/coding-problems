# 9 8 3 7 2
# 1 6 2 9 5

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[False, False] for _ in range(N)]
dp[0] = [True, True]  # 最初の要素はどちらを選んでもよい

for i in range(1, N):
    for j in range(2):
        if j == 0:
            prev_value = A[i-1]
        else:
            prev_value = B[i-1]

        # A[i]を選択する場合
        if abs(A[i] - prev_value) <= K:
            dp[i][0] |= dp[i-1][j]
        # B[i]を選択する場合
        if abs(B[i] - prev_value) <= K:
            dp[i][1] |= dp[i-1][j]


# 最後の要素でどちらか一方がTrueなら、条件を満たす数列が存在する
if dp[-1][0] or dp[-1][1]:
    print('Yes')
else:
    print('No')