
# Bの位置を調べて、それぞれのインデックスの偶奇が異なるかチェック
# KはRに挟まれてる

def k_check(s):
    if s[0] == "K" or s[-1] == "K":
        return False

    r_index = []
    k_index = 0
    for i in range(len(s)):
        if s[i] == "R":
            r_index.append(i)
        elif s[i] == "K":
            k_index = i

    return  r_index[0] < k_index < r_index[1]

def b_check(s):
    b_index = []
    for i in range(len(s)):
        if s[i] == "B":
            b_index.append(i + 1)

    b1 = b_index[0] % 2 == 0
    b2 = b_index[1] % 2 == 0

    return b1 != b2


s = input()

if k_check(s) and b_check(s):
    print("Yes")
else:
    print('No')

