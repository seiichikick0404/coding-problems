N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 数列をソート
A.sort()
B.sort()

# 最小値を初期化
curr_min = float('inf')
a_position = 0
b_position = 0

# どちらかのリストの末尾に到達するまでループ
while a_position < N and b_position < M:
    curr_diff = abs(A[a_position] - B[b_position])
    curr_min = min(curr_min, curr_diff)

    # 既に最小差が0であれば終了
    if curr_diff == 0:
        break

    # ポインタを進める
    if A[a_position] < B[b_position]:
        a_position += 1
    else:
        b_position += 1

print(curr_min)






