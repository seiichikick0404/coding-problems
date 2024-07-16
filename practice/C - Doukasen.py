N = int(input())

lines = []
total_time = 0
for i in range(N):
    A, B = map(int, input().split())
    time = A / B
    total_time += time
    lines.append((A, B))

# 二つの火がぶつかる時間
half_time = total_time / 2

# 左端からhalf_timeまでの距離を計算
current_time = 0
distance_traveled = 0
for A, B in lines:
    time = A / B
    if current_time + time >= half_time:
        # 火がぶつかる導火線の中での進行距離を計算
        distance_in_line = (half_time - current_time) * B
        distance_traveled += distance_in_line
        break
    else:
        current_time += time
        distance_traveled += A

print(distance_traveled)
