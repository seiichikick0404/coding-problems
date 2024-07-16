N = int(input())

builds = list(map(int, input().split()))

target = builds[0]
for i in range(N):
    if target < builds[i]:
        print(i+1)
        exit()

print(-1)

