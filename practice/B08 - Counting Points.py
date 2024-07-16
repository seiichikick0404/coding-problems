# 入力を受け取る
N = int(input())
MAX_COORD = 1501

# 2次元カウント配列
count_array = [[0] * MAX_COORD for _ in range(MAX_COORD)]
for _ in range(N):
    x, y = map(int, input().split())
    count_array[x][y] += 1

print(count_array)

# 2次元累積和の計算
cumulative_sums = [[0] * MAX_COORD for _ in range(MAX_COORD)]
for i in range(MAX_COORD):
    for j in range(MAX_COORD):
        cumulative_sums[i][j] = count_array[i][j] + cumulative_sums[i-1][j] + cumulative_sums[i][j-1] - cumulative_sums[i-1][j-1]

print(cumulative_sums)
# クエリへの応答
Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    # 累積和を使用して範囲内の点の数を計算
    ans = cumulative_sums[c][d] - cumulative_sums[a-1][d] - cumulative_sums[c][b-1] + cumulative_sums[a-1][b-1]
    print(ans)

