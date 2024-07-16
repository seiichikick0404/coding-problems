import math

def calculate_distance(point1, point2):
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))

def search_point(point_tuple, points):
    curr_max = 0
    max_point_idx = None
    for idx, point in enumerate(points):
        if point == point_tuple:
            continue
        distance = calculate_distance(point_tuple, point)
        if distance > curr_max:
            curr_max = distance
            max_point_idx = idx
    return max_point_idx + 1

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]


for tuple in points:
    max_len_point_idx = search_point(tuple, points)
    print(max_len_point_idx)

