N = int(input())

hash_map = {}

for i in range(N):
    score, color = map(int, input().split())
    if hash_map.get(color):
        hash_map[color] = min(hash_map[color], score)
    else:
        hash_map[color] = score

# print(hash_map)

print(max(hash_map.values()))