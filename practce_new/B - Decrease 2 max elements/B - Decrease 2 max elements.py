N = int(input())
A = list(map(int, input().split()))


total = 0
while sum(a > 0 for a in A) > 1:
    A.sort(reverse=True)
    if A[0] > 0:
        A[0] -= 1
    if A[1] > 0:
        A[1] -= 1

    total += 1

print(total)
