# フォロー、フォロー解除をシミュレーションし、特定のユーザー同士が相互フォロー状態の場合、Yes, それ以外の場合Noを返す

# {
#     1: [2],
#     2: [1, 3],
#     3: [2]
# }

N, Q = map(int, input().split())
hash_map = {}
ans = []
for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if hash_map.get(A):
            hash_map[A].add(B)
        else:
            hash_map[A] = set([B])

    elif T == 2:
        if B in hash_map.get(A, set()):
            hash_map[A].discard(B)

    else:  # T == 3のケース
        if B in hash_map.get(A, set()) and A in hash_map.get(B, set()):
            ans.append('Yes')
        else:
            ans.append('No')

for s in ans:
    print(s)


