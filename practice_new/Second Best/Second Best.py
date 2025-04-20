N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
second_best = sorted_A[-2]

print(A.index(second_best)+1)