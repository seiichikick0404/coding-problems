N = int(input())
S = input()

total = 0
for i in range(N - 2):
    if S[i] == "#" and S[i+1] == "." and S[i+2] == "#":
        total += 1

print(total)

