N, K = map(int, input().split())
A = list(map(int, input().split()))

first = A[:-K]
second = A[-K:]

print(*second + first)

