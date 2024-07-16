def dfs(v, visited, graph):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            dfs(u, visited, graph)

N, M = map(int, input().split())
graph = {i: set() for i in range(1, N+1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)


visited = set()
components = 0
for i in range(1, N+1):
    if i not in visited:
        dfs(i, visited, graph)
        components += 1

print(components)