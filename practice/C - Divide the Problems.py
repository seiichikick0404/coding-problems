N = int(input())
nums = list(map(int, input().split()))

nums.sort()
mid = (N // 2 ) - 1
mid_val1 = nums[mid]
mid_val2 = nums[mid+1]

print(mid_val2 - mid_val1)
