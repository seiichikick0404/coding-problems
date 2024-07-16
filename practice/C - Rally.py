N = int(input())
X = [int(input()) for _ in range(N)]
X.sort()

ans = float('inf')
for P in range(1, 101):
    tot = sum((x - P) ** 2 for x in X)
    ans = min(ans, tot)

print(ans)