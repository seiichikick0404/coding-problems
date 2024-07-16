
n, m = map(int, input().split())

hash_map = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    hash_map[a].append(b)
    hash_map[b].append(a)


for i in range(1, n+1):
    sorted_arr = sorted(hash_map[i])
    print(len(sorted_arr), *sorted_arr)



