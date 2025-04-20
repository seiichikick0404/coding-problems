N = int(input())
S = [list(input()) for _ in range(N)]
S.reverse()

max_j = 0
for s in S:
    max_j = max(max_j, len(s))



for j in range(max_j):
    s = ""
    for i in range(N):
        if j < len(S[i]):
            s += S[i][j]
        else:
            s += '*'

    s = s.rstrip('*')
    print(s)






