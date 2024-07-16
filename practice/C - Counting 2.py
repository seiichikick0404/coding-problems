def find_insert_position(arr, num):
    """
    Find the position where 'num' should be inserted in a sorted array 'arr' using binary search.
    """
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid

    return low

N, Q = map(int, input().split())
statures = list(map(int, input().split()))
statures.sort()

results = []
for _ in range(Q):
    val = int(input())
    index = find_insert_position(statures, val)
    results.append(N - index)

print("\n".join(map(str, results)))


