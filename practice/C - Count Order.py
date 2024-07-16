import itertools

N = int(input())

P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

t = list(itertools.permutations(range(1,N+1), N))

x = -1
y = -1
for i in range(len(t)):
    if P == t[i]:
        x = i + 1
    if Q == t[i]:
        y = i + 1

    if x is not -1 and y is not -1:
        break

print(abs(x - y))



