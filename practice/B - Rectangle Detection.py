def find_col_range(lst):
    first = -1
    last = -1

    # リストの要素をループして '#' の位置を見つける
    for i, element in enumerate(lst):
        if element == '#':
            if first == -1:
                first = i + 1
            last = i + 1

    return (first, last)

def find_row_and_col_range():
    row_start = -1
    row_end = -1
    col_start = -1
    col_end = -1

    for i in range(10):
        col_text_list = list(input())
        if "#" in col_text_list:
            # 行の範囲を設定
            if row_start == -1:
                row_start = i + 1
            row_end = i + 1

            # 列の範囲を取得
            col_range = find_col_range(col_text_list)
            if col_start == -1 or col_range[0] < col_start:
                col_start = col_range[0]
            if col_end == -1 or col_range[1] > col_end:
                col_end = col_range[1]

    return row_start, row_end, col_start, col_end

# メイン関数の実行
row_start, row_end, col_start, col_end = find_row_and_col_range()
print(row_start, row_end)
print(col_start, col_end)
