

N, M = map(int, input().split())
H = list(map(int, input().split()))

complete = 0

for i in range(N):
    if M - H[i] >= 0:
        M -= H[i]
        complete += 1
    else:
        print(complete)
        exit()

print(complete)