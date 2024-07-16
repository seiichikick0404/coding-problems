M = int(input())
days = list(map(int,input().split()))


mid_day = (sum(days) + 1) // 2

count = 0
for i in range(M):
    if mid_day <= days[i]:
        print(str(i+1) + " " + str(mid_day))
        exit()
    else:
        mid_day -= days[i]
