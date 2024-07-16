N = int(input())

hash_map = {}
for i in range(N):
    s = input()
    if s not in hash_map:
        hash_map[s] = i+1

for key, val in hash_map.items():
    print(val)
