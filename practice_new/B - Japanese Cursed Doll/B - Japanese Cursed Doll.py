n,t,p=map(int, input().split())
l = list(map(int, input().split()))
for i in range(t):
    cnt = 0
    for j in range(n):
        if l[j] + i >= t:
            cnt += 1
    if cnt >= p:
        print(i)
        break


