n = int(input())

a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))

# 二分探索関数
def bin_search(arr, target, find_first):
    start, end = 0, len(arr) - 1
    ans = len(arr)
    while start <= end:
        mid = (start + end) // 2
        if (find_first and arr[mid] < target) or (not find_first and arr[mid] <= target):
            start = mid + 1
        else:
            ans = mid
            end = mid - 1
    return ans

count = 0
for b_i in b:
    # b_iより小さいaの要素の数
    a_count = bin_search(a, b_i, True)
    # b_iより大きいcの要素の数
    c_count = len(c) - bin_search(c, b_i, False)
    # 組み合わせの総数を加算
    count += a_count * c_count

print(count)
