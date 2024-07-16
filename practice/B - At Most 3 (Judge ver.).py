n, w = map(int, input().split())
nums = list(map(int, input().split()))

ans = set()
for i in range(n):
    if nums[i] <= w:
        ans.add(nums[i])
    for j in range(i + 1, n):
        if nums[i] + nums[j] <= w:
            ans.add(nums[i] + nums[j])
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] <= w:
                ans.add(nums[i] + nums[j] + nums[k])

print(len(ans))

