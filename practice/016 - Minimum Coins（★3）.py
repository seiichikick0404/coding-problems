n = int(input())

a, b, c = map(int, input().split())
P = 9999
ans = P + 1
for x in range(P + 1):
    for y in range(P + 1):
        tmp = x * a + y * b
        if tmp % c != 0 or tmp > n:
            continue
        z = (n - tmp) // c
        if ans > x + y + z:
            ans = x + y + z



