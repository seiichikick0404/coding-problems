def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid + 1  # 1-based index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



N, X = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

index = binary_search(A, X)
print(index)