

# 二人組が隣り合っているかどうかを記録する集合
neighbors = set()

# 入力
N, M = map(int, input().split())

# 各撮影での隣り合うペアを記録
for _ in range(M):
    line = list(map(int, input().split()))
    for j in range(N - 1):
        # ソートして小さい番号が先になるようにしてからタプルを作成
        pair = tuple(sorted((line[j], line[j + 1])))
        neighbors.add(pair)

# 不仲の可能性がある二人組の数をカウント
count = 0

# 全てのペアについて調査
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        pair = (i, j)
        if pair not in neighbors:
            count += 1

# 不仲の可能性がある二人組の数を出力
print(count)
