def change_direction(direction, color):
    if color == "white":
        if direction < 4:
            return direction + 1
        else:
            return 1
    else:
        if direction > 1:
            return direction - 1
        else:
            return 4

def move(curr, direction, H, W):
    if direction == 1:  # 上
        curr[0] = (curr[0] - 1) % H
    elif direction == 2:  # 右
        curr[1] = (curr[1] + 1) % W
    elif direction == 3:  # 下
        curr[0] = (curr[0] + 1) % H
    else:  # 左
        curr[1] = (curr[1] - 1) % W
    return curr



H, W, N = map(int, input().split())

# 高さH行、横W行の配列を作成
grid = []
for i in range(H):
    arr = []
    for j in range(W):
        arr.append(".")
    grid.append(arr)

# 現在のマスに応じてシミュレーション
curr = [0, 0]
# 方向 1: 上, 2: 右, 3: 下, 4: 左
direction = 1
for i in range(N):
    if grid[curr[0]][curr[1]] == ".":
        grid[curr[0]][curr[1]] = "#"
        # 進行方向を更新
        direction = change_direction(direction, "white")
        # 現在地を更新
        curr = move(curr, direction, H, W)
    else:
        grid[curr[0]][curr[1]] = "."
        # 進行方向を更新
        direction = change_direction(direction, "black")
        # 現在地を更新
        curr = move(curr, direction, H, W)

print('\n'.join(''.join(row) for row in grid))

