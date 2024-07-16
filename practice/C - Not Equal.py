MOD = 10**9 + 7

def count_valid_sequences(N, C):
    # 初期値を1に設定（掛け算のアイデンティティ）
    total_count = 1

    # 各C[i]について、可能なA[i]の値の数を計算
    for i in range(N):
        total_count *= C[i] - i
        total_count %= MOD

    # 条件を満たさないケース（C[i] <= i）がある場合、0を返す
    if total_count < 0:
        return 0

    return total_count

# 入力例
N = int(input())
C = list(map(int, input().split()))

# ソートして、C[i] > i が常に成り立つようにする
C.sort()

print(count_valid_sequences(N, C))

