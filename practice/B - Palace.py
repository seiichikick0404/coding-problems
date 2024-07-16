
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

curr_min = float('inf')
curr_idx = 0
for i in range(N):
    temperature = T - (H[i] * 0.006)
    diff = abs(A - temperature)

    if diff < curr_min:
        curr_min = diff
        curr_idx = i


print(curr_idx+1)





