# N = int(input())

# # 1 <= Nの整数Xはいくつあるか？
# # Xの10進法記法は偶数桁で前半と後半が同じ文字列

# x_count = 0
# for x in range(1, N+1):
#     # xが偶数桁でない場合は飛ばす
#     str_x = str(x)
#     if len(str_x) % 2 != 0: continue

#     # 各桁の前半と後半を比較
#     mid = len(str_x) // 2
#     first = str_x[:mid]
#     second = str_x[mid:]

#     if first == second:
#         x_count += 1

# print(x_count)


N = int(input())
x_count = 0
x = 1  # 初期値

while True:
    str_x = str(x)
    mirror_x = int(str_x + str_x)  # 前半と後半が等しい数を生成

    if mirror_x > N:
        break

    x_count += 1
    x += 1  # 次の前半の数へ

print(x_count)
