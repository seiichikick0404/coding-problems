
# 解法1 dfs
N, M = map(int, input().split())
def dfs(N, M, start=1, arr=[]):

    # ベースケース
    if len(arr) == N:
        print(*arr)
        return

    # 再帰
    for i in range(start, M+1):
        dfs(N, M, i + 1, arr + [i])

dfs(N, M)

# n, m = map(int, input().split())
# dfs(n, m)

# 解法2ライブラリ
# from itertools import combinations
# n, m = list(map(int, input().split()))
# for l in combinations(range(1, m + 1), n):
#     print(*l, sep=' ')






