N = int(input())
P = list(map(int, input().split()))

set_nums = set()
curr_min = 0

for num in P:
    set_nums.add(num)
    while curr_min in set_nums:
        curr_min += 1
    print(curr_min)
