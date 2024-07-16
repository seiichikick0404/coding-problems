N = int(input())
A = list(map(int, input().split()))

# 前のマスの高さを記録する変数を初期化
def solve(N, A):
    for i in range(N-2, -1, -1):
        if A[i] > A[i + 1] + 1:
            return "No"
        elif A[i] == A[i + 1] + 1:
            A[i] -= 1
    return "Yes"

print(solve(N, A))