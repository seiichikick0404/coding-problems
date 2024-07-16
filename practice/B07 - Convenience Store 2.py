# 10    T -> 閉店時間
# 7     N -> 従業員数
# 0 3   L -> 労働時間
# 2 4
# 1 3
# 0 3
# 5 6
# 5 6
# 5 6

# # 閉店時間
T = int(input())

# 従業員数
N = int(input())

# イベントカウンティング用の配列
event_count = [0] * (T + 1)
print(event_count)

for _ in range(N):
    start, end = map(int, input().split())
    event_count[start] += 1  # 出勤時間でカウントを1増やす
    event_count[end] -= 1   # 退勤時間でカウントを1減らす

print(event_count)

# 累積和を計算して、各時間帯における従業員の数を求める
employees_count = 0
for count in event_count[:-1]:
    employees_count += count
    print(employees_count)




