N, M = map(int, input().split())

eat_colors = list(input().split())

set_colors = list(input().split())

prices = list(map(int, input().split()))

hash = {}
for i in range(M):
    hash[set_colors[i]] = prices[i+1]


total = 0
for i in range(N):
    if hash.get(eat_colors[i]):
        total += hash[eat_colors[i]]
    else:
        total += prices[0]

print(total)

