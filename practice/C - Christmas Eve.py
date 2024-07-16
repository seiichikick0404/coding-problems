n, k = map(int, input().split())

hights = [int(input()) for _ in range(n)]
hights = sorted(hights)

curr_diff_min = float('inf')
for i in range((n-k+1)):
    min_height = hights[i]
    max_height = hights[i + k - 1]
    diff = max_height - min_height
    curr_diff_min = min(curr_diff_min, diff)

print(curr_diff_min)
