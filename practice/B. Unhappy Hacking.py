# 2023/3/31

N = int(input())
l = list(map(int, input().split()))


dict = {}

for i in range(min(l), max(l)+1):
    cost = 0
    for j in range(N):
        cost += (abs(i-l[j]) **2)
        dict[i] = cost

ans = min(dict.values())
print(dict)
print(ans)