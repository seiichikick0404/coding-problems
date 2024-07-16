

H, W = map(int, input().split())

grid = [list(input()) for _ in range(H)]
visited = [[False]*W for _ in range(H)]

i, j = 0, 0  # 初期位置を (0, 0) とする
while True:
    if visited[i][j]:
        print(-1)
        break

    visited[i][j] = True
    direction = grid[i][j]

    if direction == 'U' and i > 0:
        i -= 1
    elif direction == 'D' and i < H - 1:
        i += 1
    elif direction == 'L' and j > 0:
        j -= 1
    elif direction == 'R' and j < W - 1:
        j += 1
    else:
        print(i + 1, j + 1)  # 1を加えて実際のグリッド位置に合わせる
        break

