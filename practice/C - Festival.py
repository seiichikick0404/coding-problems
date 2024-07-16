def next_launch(curr_day, launch_list):
    # 二分探索で次の花火が上がる日を見つける
    left, right = 0, len(launch_list) - 1
    while left < right:
        mid = (left + right) // 2
        if launch_list[mid] < curr_day:
            left = mid + 1
        else:
            right = mid
    return launch_list[left] if launch_list[left] >= curr_day else -1




n, m =  map(int, input().split())

launch_list = list(map(int, input().split()))

launch_set = set(launch_list)  # 花火が上がる日のセット

print(launch_set)

# 各日について次に花火が上がる日までの日数を計算し、出力
for curr_day in range(1, n + 1):
    if curr_day in launch_set:  # セットを使って効率的にチェック
        print(0)
    else:
        next_launch_day = next_launch(curr_day, launch_list)
        print(next_launch_day - curr_day if next_launch_day != -1 else -1)


