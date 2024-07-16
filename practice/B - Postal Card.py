
N, M =  map(int, input().split())
six_str = [input() for _ in range(N)]
three_str = [input() for _ in range(M)]

count = 0
for target_str in six_str:
    for substring in three_str:
        if target_str[-3:] == substring:
            count += 1
            break

print(count)


