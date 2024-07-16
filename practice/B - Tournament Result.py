#def is_check()

n = int(input())

wld_list = []
for _ in range(n):
    wld_list.append(input())

for i in range(n):
    for j in range(n):
        if wld_list[i][j] ==  "-": continue

        # 勝敗矛盾判定(勝ち)
        if wld_list[i][j] == "W" and wld_list[j][i] != "L":
            print("incorrect")
            exit()

        # 勝敗矛盾判定(負け)
        if wld_list[i][j] == "L" and wld_list[j][i] != "W":
            print("incorrect")
            exit()

        # 引き分け矛盾判定
        if wld_list[i][j] == "D" and wld_list[j][i] != "D":
            print("incorrect")
            exit()


print("correct")
