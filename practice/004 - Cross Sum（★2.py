H, W =  map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


# 各列の合計を計算
row_sums = [sum(row) for row in A]
col_sums = [sum(A[i][j] for i in range(H)) for j in range(W)]

# 答えを計算して出力
result = []
for i in range(H):
    result_row = []
    for j in range(W):
        # 同じ行と列の合計から自分自身を引く
        ans = row_sums[i] + col_sums[j] - A[i][j]
        result_row.append(ans)
    result.append(result_row)

# 出力形式に合わせて結果を表示
for row in result:
    print(" ".join(map(str, row)))