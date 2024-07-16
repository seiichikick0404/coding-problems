

n, q =  map(int, input().split())

hash_map = {}
for i in range(n):
    tmp = list(map(int, input().split()))
    split_l = tmp[1::]
    hash_map[i+1] = split_l

# クエリに答える
for j in range(q):
    target, val = map(int, input().split())
    print(hash_map[target][val-1])



