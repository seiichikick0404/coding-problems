N, X = map(int, input().split())

nums = set(list(map(int, input().split())))

print(nums)

for num in nums:
    print(num)
    if (num + X) in nums or (num - X) in nums:
        print('Yes')
        exit()

print('No')


