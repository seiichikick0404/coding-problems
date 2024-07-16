

N, K = map(int, input().split())
S = input()

pass_count = 0
ans = ""
for i in range(N):
    if S[i] == "o" and pass_count < K:
        ans += "o"
        pass_count += 1
        continue
    else:
        ans += "x"


print(ans)

