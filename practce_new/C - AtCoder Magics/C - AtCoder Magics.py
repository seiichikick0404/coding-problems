# 入力
n = int(input())
cards = []

for i in range(n):
    a, c = map(int, input().split())
    cards.append((a, c, i))

# コスト(c)で昇順にソート
cards.sort(key=lambda x: x[1])

# 答えを求める計算
ans = []
max_strength = 0

for a, c, idx in cards:
    if a > max_strength:
        max_strength = a
        ans.append(idx + 1)  # カード番号を 1-indexed で保持

# 結果の出力
ans.sort()
print(len(ans))
print(" ".join(map(str, ans)))




