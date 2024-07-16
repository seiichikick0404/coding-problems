N = int(input())
count = 0
for i in range(1, N+1):
    octal_representation = oct(i)
    str_8 = str(octal_representation)
    str_10 = str(i)

    # 7を含むかチェック
    if '7' not in str_8 and '7' not in str_10:
        count += 1


print(count)
