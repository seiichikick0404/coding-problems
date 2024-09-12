N, L = map(int, input().split())

for _ in range(N):
    enemy = int(input())

    if L > enemy:
        L += enemy // 2
    elif L < enemy:
        L = L // 2

print(L)