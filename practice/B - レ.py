

N, M = map(int, input().split())
re_positions = list(map(int, input().split()))

# 辺のリストを作成
edges = {}
for a in re_positions:
    if a not in edges:
        edges[a] = []
    if a+1 not in edges:
        edges[a+1] = []
    edges[a].append(a+1)
    edges[a+1].append(a)

# 深さ優先探索（DFS）で連結成分を見つける
def dfs(node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in edges.get(node, []):
        if not visited[neighbor]:
            dfs(neighbor, visited, component)

visited = [False] * (N + 1)
components = []

for i in range(1, N + 1):
    if not visited[i]:
        component = []
        dfs(i, visited, component)
        components.append(component)

# 連結成分を小さい頂点が含まれる順にソートし、各成分を大きい頂点から順に並べ替える
components.sort(key=lambda x: min(x))
ans = []
for component in components:
    ans.extend(sorted(component, reverse=True))

print(" ".join(map(str, ans)))



