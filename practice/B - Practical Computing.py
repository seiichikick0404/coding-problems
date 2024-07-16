def generate_pascals_triangle(N):
    # パスカルの三角形を格納するリストを初期化
    triangle = []

    # 各行に対して計算
    for i in range(N):
        # 現在の行を格納するリストを初期化
        row = [None] * (i + 1)
        # 行の最初と最後の要素を1に設定
        row[0], row[-1] = 1, 1

        # 中間の要素について計算
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        # 計算された行を三角形に追加
        triangle.append(row)

    return triangle

# パスカルの三角形を生成 (例: N = 5)
N = int(input())
pascals_triangle = generate_pascals_triangle(N)

# パスカルの三角形を出力
for row in pascals_triangle:
    print(*row)
