

N = int(input())

used = [False] * ((2 * N) + 2)

while True:
    for i in range(1, 2 * N + 2):
        if not used[i]:
            print(i)
            used[i] = True
            break

    aoki_score = int(input())

    if aoki_score == 0:
        exit()
    else:
        used[aoki_score] = True










