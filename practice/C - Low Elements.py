N = int(input())
P = list(map(int, input().split()))

min_val = float('inf')
ans = 0

for i in range(N):
    if P[i] <= min_val:
        min_val = P[i]
        ans += 1

print(ans)
