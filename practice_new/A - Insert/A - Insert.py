N, K, X =  map(int, input().split())
A = list(map(int, input().split()))

start = A[:K]
mid = [X]
end = A[K:]

print(*start + mid + end)

