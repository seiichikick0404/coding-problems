N = int(input())

nums = list(map(int, input().split()))

X = int(input())

val = sum(nums)

# ある程度のところまでの和を足していく
position = X // val

curr_sum = val * position
for i in range(N):
    if curr_sum + nums[i] > X:
        curr_sum += nums[i]
        print((N * position) + i+1)
        exit()
    else:
        curr_sum += nums[i]
