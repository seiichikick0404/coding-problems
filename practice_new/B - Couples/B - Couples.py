N = int(input())
A = list(map(int, input().split()))

# 同じ色の服を着た人の間に人が1人いるパターン数の合計
prevprev = A[0]
prev = A[1]
count = 0
for i in range(2, 2*N):
    curr = A[i]
    if curr != prev and curr == prevprev:
        count += 1
    prevprev = A[i+1-2]
    prev = A[i+1-1]

print(count)