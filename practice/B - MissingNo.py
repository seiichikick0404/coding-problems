
N = int(input())
list = list(map(int, input().split()))
list.sort()

for i in range(N):
    next = list[i] + 1

    if next != list[i+1]:
        print(next)
        exit()
