DIRECTIONS = [
    (-1, 0),  # 上
    (1, 0),   # 下
    (0, -1),  # 左
    (0, 1),   # 右
    (-1, -1), # 左上
    (-1, 1),  # 右上
    (1, -1),  # 左下
    (1, 1)    # 右下
]

def count_squares(n, r_q, c_q, obstacles_set):
    count = 0
    for dr, dc in DIRECTIONS:
        # 現在の位置
        r, c = r_q, c_q
        while True:
            r += dr
            c += dc
            # 範囲外または障害物で停止
            if r < 1 or r > n or c < 1 or c > n or (r, c) in obstacles_set:
                break
            count += 1
    return count



def queensAttack(n, k, r_q, c_q, obstacles):
    # 障害物をセットに変換
    obstacles_set = set((r, c) for r, c in obstacles)

    # 到達可能なマスを数える
    return count_squares(n, r_q, c_q, obstacles_set)





n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [
    [5, 5],
    [4, 2],
    [2, 3]
]

result = queensAttack(n, k, r_q, c_q, obstacles)
print(result)