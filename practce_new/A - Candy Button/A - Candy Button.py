N, C = map(int, input().split())
T = list(map(int, input().split()))

total = 0
last_push = 1000
for curr_time in T:
    if abs(last_push - curr_time) >= C:
        total += 1
        last_push = curr_time

print(total)

