def find_day(n, k, medicines):
    ok = 1 << 30  # 初期化された上限値
    ng = 0  # 初期化された下限値
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        sum = 0
        for duration, pills_per_day in medicines:
            if mid <= duration:
                sum += pills_per_day
        if sum <= k:
            ok = mid
        else:
            ng = mid
    return ok

# 入力例
n, k = map(int, input().split())
medicines = [tuple(map(int, input().split())) for _ in range(n)]

print(find_day(n, k, medicines))