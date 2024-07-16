N = int(input())
S = list(input())

result = [S[0]]

for i in range(1, N):
    if S[i] != S[i-1]:
        result.append(S[i])

print(len(result))