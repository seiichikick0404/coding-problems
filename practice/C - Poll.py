n = int(input())
hash_map = {}
str_list = []
max_num = 0
for i in range(n):
    s = input()
    str_list.append(s)
    if hash_map.get(s):
        hash_map[s] += 1
    else:
        hash_map[s] = 1

    max_num = max(hash_map[s], max_num)

ans = set()
for s in str_list:
    if hash_map[s] == max_num:
        ans.add(s)

ans = sorted(ans)

for s in ans:
    print(s)


