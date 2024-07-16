N = int(input())
nums = list(map(int, input().split()))

ans = []

# 隣り合う値同士を合成してできた値を使いさらに合成して最後の一つになるまでループする
while len(nums) > 1:
    nums.sort()
    new_content = (nums[0] + nums[1]) / 2
    nums.pop(0)
    nums.pop(0)

    nums.append(new_content)

print(nums[0])


