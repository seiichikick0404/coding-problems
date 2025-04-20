# 入力の読み込み
H, W = map(int, input().split())
Si, Sj = map(int, input().split())
grid = [input().strip() for _ in range(H)]
X = input().strip()

# 現在の位置を1-indexedから0-indexedに変換
current_i, current_j = Si - 1, Sj - 1

# 各指示に従って移動
for move in X:
    if move == 'L' and current_j > 0 and grid[current_i][current_j - 1] == '.':
        current_j -= 1
    elif move == 'R' and current_j < W - 1 and grid[current_i][current_j + 1] == '.':
        current_j += 1
    elif move == 'U' and current_i > 0 and grid[current_i - 1][current_j] == '.':
        current_i -= 1
    elif move == 'D' and current_i < H - 1 and grid[current_i + 1][current_j] == '.':
        current_i += 1

# 最終位置を出力 (0-indexedを1-indexedに戻す)
print(current_i + 1, current_j + 1)