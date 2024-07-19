N, L, R = map(int, input().split())

l = [i for i in range(1, N+1)]

# left, right, midに分解する
left = l[:L-1]
mid = l[L-1:R]
right = l[R:]

mid = sorted(mid, reverse=True)

result = left + mid + right

print(*result)
