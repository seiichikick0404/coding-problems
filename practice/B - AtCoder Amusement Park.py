# N: グループ数, K: 席数
N, K = map(int, input().split())

# 各グループ毎の人数
groupies = list(map(int, input().split()))

total = 0
curr_seat = K
for i in range(N):
    if curr_seat < groupies[i]:
        total += 1
        curr_seat = K

    curr_seat -= groupies[i]

total += 1

print(total)







