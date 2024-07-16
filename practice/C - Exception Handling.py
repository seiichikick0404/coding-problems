def _main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # 左方向から見たときの最大値
    lft = A.copy()
    for i in range(1, N):
        lft[i] = max(lft[i], lft[i-1])

    # 右方向から見たときの最大値
    rht = A.copy()
    for i in range(N-2, -1, -1):
        rht[i] = max(rht[i], rht[i+1])

    # 各要素を除いた場合の最大値を計算して出力
    for i in range(N):
        ans = -1
        if i > 0:
            ans = max(ans, lft[i-1])
        if i+1 < N:
            ans = max(ans, rht[i+1])
        print(ans)