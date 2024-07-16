N = int(input())
nums = list(map(int, input().split()))

hash_map = {}
for i in range(N):
    hash_map[nums[i]] = i + 1

ans = []

for i in range(1, N+1):
    ans.append(hash_map[i])

print(*ans)