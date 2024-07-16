S = input()
T = input()
n = len(S)

shift_amount = (ord(T[0]) - ord(S[0])) % 26

# S と T の全ての文字に対して、一貫したシフト量があるかチェック
for i in range(1, n):
    if (ord(T[i]) - ord(S[i])) % 26 != shift_amount:
        print("No")
        exit()

print('Yes')


