N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

first_times = [float('inf')] * N

for i in range(N):
    first_times[i] = min(first_times[i], T[i])

for _ in range(2):
    for i in range(N):
        next_i = (i + 1) % N
        first_times[next_i] = min(first_times[next_i], first_times[i] + S[i])
        
for time in first_times:
    print(time)
