import math

A, B, H, M = map(int, input().split())

# 短針と長針の角度をラジアンで計算
angle_hour = math.radians((H % 12) * 30 + M * 0.5)
angle_minute = math.radians(M * 6)

# 各針の座標を計算
hour_x = A * math.cos(angle_hour)
hour_y = A * math.sin(angle_hour)
minute_x = B * math.cos(angle_minute)
minute_y = B * math.sin(angle_minute)

# 2点間の距離を計算
distance = math.sqrt((hour_x - minute_x) ** 2 + (hour_y - minute_y) ** 2)
print(distance)
