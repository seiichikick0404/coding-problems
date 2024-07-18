N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result_a = [(A[i], "A") for i in range(N)]
result_b = [(B[i], "B") for i in range(M)]

result_ab = result_a + result_b
result_ab = sorted(result_ab, key=lambda x: x[0])

for i in range(N+M - 1):
    if result_ab[i][1] == "A" and result_ab[i+1][1] == "A":
        print('Yes')
        exit()

print('No')
