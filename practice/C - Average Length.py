from itertools import permutations
import math

N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

total_distance = 0
for ord in permutations(range(N)):
    for i in range(N - 1):
        a, b = ord[i], ord[i + 1]
        dx, dy = coordinates[a][0] - coordinates[b][0], coordinates[a][1] - coordinates[b][1]
        total_distance += math.sqrt(dx**2 + dy**2)

# 平均距離の計算
average_distance = total_distance / math.factorial(N)
print(f"{average_distance:.10f}")