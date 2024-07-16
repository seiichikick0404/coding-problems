N, S, M, L = map(int, input().split())

curr_min = 10**8
for a in range(101):
    for b in range(101):
        for c in range(101):
            if 6*a + 8*b + 12*c >= N:
                curr_min =  min(curr_min, a*S + b*M + c*L)

print(curr_min)