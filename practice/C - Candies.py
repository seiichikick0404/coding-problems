def max_candies_dp(N, A):
    dp = [[0 for _ in range(N)] for _ in range(2)]
    
    dp[0][0] = A[0][0]
    for y in range(2):
        for x in range(N):
            if x > 0:
                dp[y][x] = max(dp[y][x], dp[y][x-1] + A[y][x])
            if y > 0:
                dp[y][x] = max(dp[y][x], dp[y-1][x] + A[y][x])
    
    return dp[1][N-1]

N = int(input())
grid = [list(map(int, input().split())) for _ in range(2)]

print(max_candies_dp(N, grid))