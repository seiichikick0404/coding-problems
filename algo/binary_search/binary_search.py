def binary_search(arr, x):
    start =  0
    end = len(arr) -1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1


l = [10, 24, 34, 47, 50]
print(binary_search(l, 50))


