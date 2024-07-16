n, k, x = map(int, input().split())
a = [0] + list(map(int, input().split()))  # インデックス1から始めるために0を先頭に追加

ans = sum(a)  # 全商品の合計金額

# クーポンで割引可能な最大金額を計算
m = sum(ai // x for ai in a)
m = min(m, k)
ans -= m * x
k -= m

# クーポン適用後の各商品の価格を計算
for i in range(1, n+1):
    a[i] %= x

# 価格が小さい商品からクーポンを適用
a.sort(reverse=True)  # 降順にソート

for i in range(n):
    if k == 0:
        break
    ans -= a[i]
    k -= 1

print(ans)
