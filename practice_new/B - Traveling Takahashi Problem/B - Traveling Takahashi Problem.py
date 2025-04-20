import math

def calc_cost(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]
coordinates.insert(0, (0, 0))
coordinates.append((0, 0))

total_cost = 0
curr_coordinate = None
next_coordinate = None
for i in range(len(coordinates) - 1):
    curr_coordinate = coordinates[i]
    next_coordinate = coordinates[i+1]
    cost = calc_cost(curr_coordinate, next_coordinate)
    total_cost += cost

print(total_cost)



