
# 入力
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# クッキーが置かれている最小および最大の行と列を特定
min_row, max_row = H, 0
min_col, max_col = W, 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

# 部分長方形内でクッキーがないマスを探す
for i in range(min_row, max_row + 1):
    for j in range(min_col, max_col + 1):
        if grid[i][j] == ".":
            print(i+1, j+1)
            break

