



N = int(input())


for i in range(N):
    q_num = int(input())
    nums = list(map(int, input().split()))

    count = 0
    for num in nums:
        if num % 2 != 0:
            count += 1

    print(count)

