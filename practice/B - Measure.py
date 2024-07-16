

N = int(input())

divisors = [i for i in range(1, 10) if N % i == 0]

ans = []
for i in range(N + 1):
    flag = False

    for j in divisors:
        if i % (N // j) == 0:
            ans.append(str(j))
            flag = True
            break

    if not flag:
        ans.append('-')

print(''.join(ans))





