
N, A = map(int, input().split())
T = list(map(int, input().split()))

curr_time = 0
for i in range(N):
    if curr_time < T[i]:
        # 次の人がチケットの列に並ぶまで時間を進める
        curr_time = T[i]

    curr_time += A
    print(curr_time)