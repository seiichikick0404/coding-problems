N, K = input().split()
K = int(K)


for i in range(K):
    g1 = int("".join(sorted(str(N), reverse=True)))
    g2 = int("".join(sorted(str(N))))
    N = g1 - g2

print(N)


# s = "54321"
# print(int("".join(sorted(s))))