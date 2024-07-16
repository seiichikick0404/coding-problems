q_num = int(input())

ans = []
for i in range(q_num):
    q, x = map(int, input().split())
    if q == 1:
        ans.append(x)
    else:
        print(ans[-x])

