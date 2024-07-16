N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

# x, y 座標の計算
x = [[(B[i][j] + 6) // 7 for j in range(M)] for i in range(N)]
y = [[(B[i][j] - 1) % 7 + 1 for j in range(M)] for i in range(N)]

ans = "Yes"
for i in range(N):
    for j in range(M):
        if i > 0 and x[i][j] != x[i-1][j] + 1:
            ans = "No"
        if j > 0 and y[i][j] != y[i][j-1] + 1:
            ans = "No"
        # 横に連続する要素が同じ行にあるかチェック
        if j > 0 and x[i][j] != x[i][j-1]:
            ans = "No"
        # 縦に連続する要素が同じ列にあるかチェック
        if i > 0 and y[i][j] != y[i-1][j]:
            ans = "No"

print(ans)


