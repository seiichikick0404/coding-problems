# 解法1
# N = int(input())
# A = list(map(int, input().split()))

# curr = 0
# for val in A:
#     curr += val
#     if curr < 0:
#         curr = 0

# print(curr)

# 解法2 累積和
n = int(input())  # 入力される整数の数
a = list(map(int, input().split()))  # 各整数の入力

m = 0  # 最小累積和を格納する変数
sum = 0  # 現在の累積和を格納する変数

for e in a:
    sum += e  # 累積和を更新
    m = min(m, sum)  # 最小累積和を更新

print(max(0, sum - m))
