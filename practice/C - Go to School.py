N = int(input())
nums = list(map(int, input().split()))

hash_map = {}
for i in range(1, N+1):
    hash_map[i] = nums[i-1]

ans = sorted(hash_map.items(), key=lambda x:x[1])


print(' '.join(str(ans[i][0]) for i in range(N)))
