N, Q = map(int, input().split())

nums = list(map(int, input().split()))

queries = []
for i in range(Q):
    x, k = map(int, input().split())
    queries.append((x, k))

hash_map = {}
for i in range(N):
    if hash_map.get(nums[i]):
        hash_map[nums[i]].append(i)
    else:
        hash_map[nums[i]] = [i]

for query in queries:
    x, k = query
    if hash_map.get(x) and len(hash_map[x]) >= k:
        print(hash_map[x][k-1] + 1)
    else:
        print(-1)


