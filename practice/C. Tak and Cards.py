# 2023 4/10
# かなり難しい というか解けなかった

N, A = map(int, input().split())
x = list(map(int, input().split()))

dp = [[[0]*3010 for j in range(N+1)] for i in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(N):
        for k in range(2500):
            if dp[i][j][k]:
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j+1][k+x[i]] += dp[i][j][k]

ans = 0
for i in range(1, N+1):
    ans += dp[N][i][i*A]

print(ans)
