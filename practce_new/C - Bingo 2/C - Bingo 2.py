N, T = map(int, input().split())
A = list(map(int, input().split()))

row_count = [0] * N
col_count = [0] * N
main_diag_count = 0
anti_diag_count = 0
marked_positions = set()

for turn in range(T):
    a = A[turn]
    a -= 1  # 0-indexedに変換
    row = a // N
    col = a % N

    # すでに印が付いているなら無視
    if (row, col) in marked_positions:
        continue

    # 印を付ける
    marked_positions.add((row, col))
    row_count[row] += 1
    col_count[col] += 1

    # 主対角線
    if row == col:
        main_diag_count += 1
    # 副対角線
    if row + col == N - 1:
        anti_diag_count += 1

    # ビンゴ達成のチェック
    if row_count[row] == N or col_count[col] == N or main_diag_count == N or anti_diag_count == N:
        print(turn + 1)
        print(marked_positions)
        exit()

print(-1)  # ビンゴが達成されない場合