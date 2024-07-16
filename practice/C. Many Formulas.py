S = input()
N = len(S)

ans = 0
for i in range(1 << (N - 1)):
    sm = 0
    a = int(S[0])
    for j in range(N - 1):
        if i & (1 << j):
            sm += a
            a = 0
        a = a * 10 + int(S[j + 1])
    sm += a
    ans += sm

print(ans)

