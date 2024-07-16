
H, W =  map(int, input().split())

ans = []

for i in range(H):
    tmp = list(input())
    ans.append(tmp)

count = 0
ans_l = []
for i in range(W):
    count = 0
    for j in range(H):
        if ans[j][i] == "#":
            count += 1
    ans_l.append(count)


print(*ans_l)
    