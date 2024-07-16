# 2023 4/20

N = int(input())
min_votes = [1, 1]  # 初期値はそれぞれ1票ずつ入っていると仮定する

for i in range(N):
    Ti, Ai = map(int, input().split())
    # 得票数の比から、高橋くんと青木くんの得票数を求める
    # 高橋くんの得票数 = Ti * a / gcd(Ti, Ai)
    # 青木くんの得票数 = Ai * a / gcd(Ti, Ai)
    a = max(-(-min_votes[0] // Ti), -(-min_votes[1] // Ai))
    print("Ti = " + str(Ti))
    print("Ai = " + str(Ai))
    print("min_votes[0] // Ti = " + str(-(-min_votes[0] // Ti)))
    print("min_votes[1] // Ai = " + str(-(-min_votes[0] // Ai)))
    print("aの値は" + str(a) + "です")
    print("[" + str(Ti * a) + ", " + str(Ai * a) + "]")
    min_votes = [Ti * a, Ai * a]  # 得票数を更新する

print(sum(min_votes))