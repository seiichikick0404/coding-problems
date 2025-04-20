N, T, A = map(int, input().split())

valid_count = N - (T + A)

min_score = min([T, A]) + valid_count
max_score = max([T, A])

if min_score < max_score:
    print('Yes')
else:
    print('No')

