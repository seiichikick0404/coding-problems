# 縦チェック


# 横チェック


# 斜めチェック





H, W = map(int, input().split())

def find_snuke(grid, H, W):
    # Directions for s, n, u, k, e sequence: right, down, right-down-diagonal, left-down-diagonal
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for i in range(H):
        for j in range(W):
            for dx, dy in directions:
                # Check if 'snuke' can be formed starting at (i, j) in the current direction
                if all(0 <= i + k * dx < H and 0 <= j + k * dy < W and grid[i + k * dx][j + k * dy] == char 
                       for k, char in enumerate("snuke")):
                    # Return the 1-indexed position (i + 1, j + 1)
                    return i + 1, j + 1

    return -1, -1  # If 'snuke' is not found



find_snuke(grid, H, W)