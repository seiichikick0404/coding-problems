n = int(input())  # 元素の数を入力
a = [[0] * n for _ in range(n)]  # 2次元配列aを初期化

# 合成結果を入力
for i in range(n):
    row = list(map(int, input().split()))  # 1行分の入力を受け取る
    for j in range(i + 1):  # 下三角行列部分のみ埋める
        a[i][j] = row[j] - 1  # 0-basedに変換

ans = 0  # 最初は元素1 (0-basedでは0)

# 合成処理
for i in range(n):
    if ans >= i:
        ans = a[ans][i]
    else:
        ans = a[i][ans]

ans += 1  # 1-basedに戻す

# 最終的な結果を出力
print(ans)

