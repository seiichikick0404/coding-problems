# 2022/3/29

N, A, B = map((int), input().split())
N = N+1

hashMap = {
    "A": A,
    "B": B,
    }

winner = ""
for i in range(N):
    #Aの処理
    if hashMap["A"] + 1 != hashMap["B"]: hashMap["A"] += 1
    elif hashMap["A"] - 1 >= 1: hashMap["A"] -= 1
    else:
        winner = "Borys"
        break

    # Bの処理
    if hashMap["B"] - 1 != hashMap["A"]: hashMap["B"] -= 1
    elif hashMap["B"] + 1 <= N: hashMap["B"] += 1
    else:
        winner = "Alice"
        break


print(winner)