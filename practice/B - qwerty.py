P = list(map(int, input().split()))

hash_map = {i: chr(96 + i) for i in range(1, 27)}

ans = ""
for i in range(len(P)):
    ans += hash_map[P[i]]

print(ans)