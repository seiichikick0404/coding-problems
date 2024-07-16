import math

N = int(input())

ans = []
# Nの平方根までの約数を探す
for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        ans.append(N // i)
        # 平方根自体は二回追加しないようにする
        if i != N // i:
            ans.append(i)

# 逆順で出力
ans.sort()
for a in ans:
    print(a)