

l = list(map(int, input().split()))

if len(set(l)) < 2:
    print(-1)
    exit()


for i in range(1, 4):
    if i not in l:
        print(i)
        exit()


