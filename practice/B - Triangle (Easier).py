n, m = map(int, input().split())
adj = [[False] * n for _ in range(n)]



for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u][v] = True
    adj[v][u] = True


ans = 0

for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            if adj[a][b] and adj[b][c] and adj[c][a]:
                ans += 1

print(ans)