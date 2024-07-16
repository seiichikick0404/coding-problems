A, B, AB, X, Y = map(int, input().split())

# ABを優先的に購入する戦略
ans1 = AB * (min(X, Y) * 2)
if X < Y:
    ans1 += (Y-X) * B
else:
    ans1 += (X-Y) * A

# ABのみで構成する戦略
ans2 = AB * (max(X, Y) * 2)


# A, Bそれぞれを愚直に購入する戦略
ans3 = (A * X) + (B * Y)

# 比較して安い方を出力
print(min(ans1, ans2, ans3))