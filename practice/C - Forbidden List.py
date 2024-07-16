X, N = map(int, input().split())
p = set(map(int, input().split()))

ans = float('inf')
diff = float('inf')

for y in range(102):
    if y not in p:
        d = abs(y - X)
        if d < diff:
            ans = y
            diff = d

print(ans)
