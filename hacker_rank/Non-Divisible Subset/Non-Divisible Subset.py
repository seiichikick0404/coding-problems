def nonDivisibleSubset(k, s):
    # 余りのカウント
    remainder_count = [0] * k
    for num in s:
        remainder_count[num % k] += 1

    # 最大部分集合のサイズを計算
    subset_size = 0

    # 余りが0の場合、1つだけ選択可能
    if remainder_count[0] > 0:
        subset_size += 1

    # 余りが x と k-x のペアを処理
    for i in range(1, (k // 2) + 1):
        if i == k - i:  # 余りが k/2 の場合
            subset_size += 1
        else:
            subset_size += max(remainder_count[i], remainder_count[k - i])

    return subset_size



k = 3
s = [1, 7, 2, 4]
result = nonDivisibleSubset(k, s)
print(result)