def count_combinations(N, P, Q, A):
    ans = 0
    for i in range(N):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        if A[i] * A[j] % P * A[k] % P * A[l] % P * A[m] % P == Q:
                            ans += 1
    return ans

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

print(count_combinations(N, P, Q, A))




