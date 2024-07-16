
# N, D = map(int, input().split())
# S = [input() for _ in range(N)]

# ans = 0
# cur = 0
# for j in range(D):
#     can = 1
#     for i in range(N):
#         can &= S[i][j] == 'o'
#     if can:
#         cur += 1
#     else:
#         cur = 0
#     ans = max(ans, cur)

# print(S)
# print(ans)





N, D = map(int, input().split())
days = [input() for _ in range(N)]

ans = 0
cur = 0

for j in range(D):
    flag = True
    
    for i in range(N):
        if days[i][j] != "o":
            flag = False

    if flag:
        cur += 1
    else:
        cur = 0

    ans = max(ans, cur)

print(ans)

    
