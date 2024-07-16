K, N = map(int, input().split())

A = list(map(int, input().split()))

# 区間距離を計算
# 隣接する家間の距離を計算
distances = [A[i+1] - A[i] for i in range(N-1)] + [A[0] + K - A[N-1]]

# 最大の隣接距離を見つける
max_distance = max(distances)

# 最短距離を計算
shortest_distance = K - max_distance

print(shortest_distance)