N, L = map(int, input().split())

dp = [0] * (N + 1)
dp[0] = 1
MOD = 1000000007
for i in range(1, N + 1):
    # i-1段目から1段上る方法
    dp[i] += dp[i - 1]

    # i-L段目からL段上る方法
    if i >= L:
        dp[i] += dp[i - L]
    dp[i] %= MOD  # MODで割った余りを取る

print(dp)

print(dp[N])

