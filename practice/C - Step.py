
N = int(input())
A = list(map(int, input().split()))

max_height = 0  # 現在までの最大身長
total_stool_height = 0  # 踏み台の高さの合計

for i in range(N):
    if A[i] > max_height:
        max_height = A[i]  # 最大身長の更新
    else:
        total_stool_height += max_height - A[i]  # 必要な踏み台の高さを加算

print(total_stool_height)
