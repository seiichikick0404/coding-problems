



n = int(input())
a = [0] + [int(x) for x in input().split()]  # インデックス1から始めるために先頭に0を追加

# 各人が呼ばれたかどうかを追跡するためのリスト
b = [False] * (n + 1)

# aの各要素について、対応する人が呼ばれたことを記録
for i in range(1, n + 1):
    if not b[i]:
        b[a[i]] = True

# 呼ばれなかった人を数えてリストアップ
k = 0
uninvoked = []
for i in range(1, n + 1):
    if not b[i]:
        k += 1
        uninvoked.append(i)

# 結果を出力
print(k)
print(" ".join(map(str, uninvoked)))

