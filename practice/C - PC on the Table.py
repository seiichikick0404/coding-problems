H, W = map(int, input().split())

grid = [list(input()) for _ in range(H)]

ans = []
for i in range(H):
    dup_flag = False
    for j in range(W - 1):
        if grid[i][j] == "T" and grid[i][j+1] == "T":
            grid[i][j] = "P"
            grid[i][j+1] = "C"

for row in grid:
    print(''.join(row))
