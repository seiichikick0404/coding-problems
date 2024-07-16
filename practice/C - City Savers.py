def solve(n, a, b):
    ans = 0
    for i in range(n):
        # 勇者iが倒せる数が残っていないときは次の勇者へ
        if b[i] == 0:
            continue

        # 勇者iが倒せる数が残っているモンスターの数より少ないときは倒せるだけ倒す
        # 都市iのモンスターを倒しきれないとき
        if b[i] <= a[i]:
            ans += b[i]
            a[i] -= b[i]  # 実際にモンスターを倒した分を減算
            continue

        # 都市iのモンスターは倒せるが都市i+1のモンスターは倒しきれないとき
        if b[i] <= a[i] + a[i+1]:
            ans += b[i]
            b[i] -= a[i]
            a[i+1] -= b[i]
            continue

        # 勇者iが都市i, i+1のモンスターをすべて倒しきれるときはすべて倒す
        ans += a[i] + a[i+1]
        a[i+1] = 0  # 都市i+1のモンスターをすべて倒したことにする

    return ans
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(solve(N, A, B))

