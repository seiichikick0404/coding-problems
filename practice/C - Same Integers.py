# nums = list(map(int, input().split()))

# def min_operations_to_equal_integers(A, B, C):
#     # Sort the numbers to make it easier to apply operations
#     nums = sorted([A, B, C])

#     # Step 1: Make all numbers have the same parity (even or odd) by applying operations if needed
#     # Calculate the total number of operations needed to make them have the same parity
#     operations = 0
#     while len(set([num % 2 for num in nums])) > 1:
#         # If there's a mix of even and odd, increase the two smallest numbers (which makes them have the same parity as the largest)
#         nums[0] += 1
#         nums[1] += 1
#         operations += 1
#         nums.sort()

#     # Step 2: Once all numbers have the same parity, we can make them equal
#     # The strategy is to make the smallest numbers catch up to the largest by increasing them
#     while len(set(nums)) > 1:
#         # Difference between the largest and the smallest numbers
#         diff = nums[2] - nums[0]

#         # If the difference is 2 or more, we can increase the smallest number by 2
#         # or increase the two smallest numbers by 1 each (which is always better or equal)
#         if diff >= 2:
#             nums[0] += 2
#         else:
#             nums[0] += 1
#             nums[1] += 1
#         operations += 1
#         nums.sort()

#     return operations

# # Test the function with the provided examples
# test_cases = [
#     (2, 5, 4),
#     (2, 6, 3),
#     (31, 41, 5)
# ]


def min_operations_to_equalize_v2(v):
    odd = even = 0
    for i in v:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    ans = 0

    # 調整
    if odd == 2:
        ans += 1
        for i in range(3):
            if v[i] % 2 == 1:
                v[i] += 1
    elif even == 2:
        ans += 1
        for i in range(3):
            if v[i] % 2 == 0:
                v[i] += 1

    ma = max(v)
    for i in v:
        ans += (ma - i) // 2

    return ans


nums = list(map(int, input().split()))
print(min_operations_to_equalize_v2(nums))


































