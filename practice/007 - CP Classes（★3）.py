import bisect

N = int(input())
rating_list = list(map(int, input().split()))
rating_list.sort()

Q = int(input())

for i in range(Q):
    target = int(input())
    target_index = bisect.bisect_left(rating_list, target)

    if target_index == 0:
        print(abs(rating_list[0] - target))
    elif target_index == N:
        print(abs(rating_list[-1] - target))
    else:
        # 前後の絶対値の差を比較
        prev = abs(rating_list[target_index - 1] - target)
        next = abs(rating_list[target_index] - target)
        print(min(prev, next))




