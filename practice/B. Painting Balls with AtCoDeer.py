# 2022 4/19 解けなかった
N, K = map(int, input().split())


total = K
for i in range(N-1):
    print(str(total) + " ✖︎ " + str(K-1) + " = " + str(total * (K-1)))
    total = total * (K-1)

print(total)