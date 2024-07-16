n = int(input())
employees = list(map(int, input().split()))

hash_map = {}
for i in range(n-1):
    if hash_map.get(employees[i]):
        hash_map[employees[i]] += 1
    else:
        hash_map[employees[i]] = 1


for i in range(1, n+1):
    if hash_map.get(i):
        print(hash_map[i])
    else:
        print(0)

