

N = int(input())
l = list(map(int, input().split()))
ans = []

i = 0
while i < N:
    ans.append(l[i])
    if i < N - 1 and abs(l[i] - l[i + 1]) > 1:
        if l[i] < l[i + 1]:
            ans.extend(range(l[i] + 1, l[i + 1]))
        else:
            ans.extend(range(l[i] - 1, l[i + 1], -1))
    i += 1

print(*ans)
