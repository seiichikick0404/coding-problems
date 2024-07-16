N = int(input())

# 各桁の合計を計算
digit_sum = sum(map(int, str(N)))

# 各桁の合計が3の倍数であれば、0桁を消去する
if digit_sum % 3 == 0:
    print(0)
    exit()

# Nの桁数
num_digits = len(str(N))

# 1桁を消去して3の倍数を作れるかチェック
if num_digits > 1:
    for digit in str(N):
        if (digit_sum - int(digit)) % 3 == 0:
            print(1)
            exit()

# 2桁を消去して3の倍数を作れるかチェック
if num_digits > 2:
    for i in range(num_digits):
        for j in range(i + 1, num_digits):
            if (digit_sum - int(str(N)[i]) - int(str(N)[j])) % 3 == 0:
                print(2)
                exit()

# どの桁を消去しても3の倍数にならない場合
print(-1)