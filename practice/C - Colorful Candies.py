n, k = map(int, input().split())
c = list(map(int, input().split()))

mp = {}
# 初期ウィンドウの色の出現回数をカウント
for i in range(k):
    mp[c[i]] = mp.get(c[i], 0) + 1

ans = len(mp)

# スライディングウィンドウ
for i in range(k, n):
    # 新しいキャンディの色を追加
    mp[c[i]] = mp.get(c[i], 0) + 1
    # 古いキャンディの色を削除
    mp[c[i-k]] -= 1
    if mp[c[i-k]] == 0:
        del mp[c[i-k]]
    # 色の種類数の最大値を更新
    ans = max(ans, len(mp))

print(ans)
