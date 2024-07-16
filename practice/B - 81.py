N = int(input())

for i in range(1, 9+1):
    for j in range(i, 9+1):
        if i * j == N:
            print('Yes')
            exit()

print('No')