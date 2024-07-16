def compare_grades_optimized(N, K, A):
    results = []
    prev_product = 1

    # 最初のK個の要素の積を計算
    for i in range(K):
        prev_product *= A[i]

    # K+1学期以降の評点を計算して比較
    for i in range(K, N):
        current_product = prev_product * A[i] // A[i - K]
        if current_product > prev_product:
            results.append("Yes")
        else:
            results.append("No")
        prev_product = current_product

    return results



N, K = map(int, input().split())
A = list(map(int, input().split()))

arr = compare_grades_optimized(N, K, A)

for val in arr:
    print(val)



