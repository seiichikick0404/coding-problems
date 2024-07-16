def round_to_nearest_max_special(X, K):
    for i in range(K):
        # 四捨五入の係数を計算する (10^(i+1))
        round_factor = 10 ** (i + 1)

        # 下限倍率と上限倍率を計算する
        lower_multiple = (X // round_factor) * round_factor
        upper_multiple = lower_multiple + round_factor

        # 差の絶対値が最小の倍数を選び、等しい場合は大きい方を選ぶ。
        if abs(upper_multiple - X) <= abs(X - lower_multiple):
            X = upper_multiple
        else:
            X = lower_multiple

    return X

X, K = map(int, input().split())
ans = round_to_nearest_max_special(X, K)

print(ans)

