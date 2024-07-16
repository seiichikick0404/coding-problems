

def explode_bombs(row, col, grid):
    # 爆発の影響を受けるマスを記録するためのセット
    to_explode = set()

    # 各爆弾の位置と威力を確認し、影響範囲をセットに追加
    for i in range(row):
        for j in range(col):
            if grid[i][j].isdigit():
                power = int(grid[i][j])
                for di in range(-power, power + 1):
                    for dj in range(abs(di) - power, power - abs(di) + 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < row and 0 <= nj < col:
                            to_explode.add((ni, nj))

    # 爆発の影響を受けるマスを空きマスに更新
    for i, j in to_explode:
        grid[i][j] = '.'

    return grid

# 入力を読み込む
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# 爆弾を爆発させる
result = explode_bombs(R, C, board)

# 結果を出力
for row in result:
    print("".join(row))
