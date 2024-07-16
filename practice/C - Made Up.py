def solve(N, A, B, C):
    # インデックスを0ベースに調整
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    C = [c - 1 for c in C]

    # B[C[j]]の出現回数をカウント
    count = [0] * N
    for j in range(N):
        count[B[C[j]]] += 1

    print(count)

    # A[i]が指すcountの値を合計
    ans = 0
    for i in range(N):
        ans += count[A[i]]

    return ans

# 標準入力からデータを読み込む
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 結果を出力
print(solve(N, A, B, C))
