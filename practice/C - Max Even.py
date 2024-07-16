
# N = int(input())

# nums = list(map(int, input().split()))

# max_progress = -1
# for i in range(N):
#     for j in range(N):
#         if i == j: continue

#         if (nums[i] + nums[j]) % 2 == 0:
#             max_progress = max(nums[i] + nums[j], max_progress)

# print( max_progress)


N = int(input())

nums = sorted(list(map(int, input().split())))

progress_list = []
odd_list = []
for i in range(N):
    if nums[i] % 2 == 0:
        progress_list.append(nums[i])
    else:
        odd_list.append(nums[i])

max_progress = 0
if len(progress_list) > 1:
    max_progress = progress_list[-1] + progress_list[-2]

max_odd = 0
if len(odd_list) > 1:
    max_odd = odd_list[-1] + odd_list[-2]


if max_progress == 0 and max_odd == 0:
    print(-1)
else:
    print(max(max_progress, max_odd))

