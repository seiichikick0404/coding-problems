N, K, Q = map(int, input().split())

ans = [K] * N
for i in range(Q):
    winner_index = int(input())
    winner_index -= 1

    ans[winner_index] += 1

for i in range(N):
    ans[i] -= Q

for score in ans:
    if score >= 1:
        print("Yes")
    else:
        print("No")