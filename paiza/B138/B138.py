H, W = map(int, input().split())
l = [list(input()) for _ in range(H)]

# ドーナツの条件を満たすかどうかを判定する関数
def is_donut(l, h, w):
    # 3x3の領域が範囲内に収まるか確認
    if h > 0 and h < H-1 and w > 0 and w < W-1:
        # 中央が白で、周囲8マスが黒かどうか確認
        if l[h][w] == '.' and \
           l[h-1][w-1] == '#' and l[h-1][w] == '#' and l[h-1][w+1] == '#' and \
           l[h][w-1] == '#' and l[h][w+1] == '#' and \
           l[h+1][w-1] == '#' and l[h+1][w] == '#' and l[h+1][w+1] == '#':
            return True
    return False

# ドーナツの数を数える
count = 0
for h in range(1, H-1):
    for w in range(1, W-1):
        if is_donut(l, h, w):
            count += 1

# 結果を表示
print(count)
