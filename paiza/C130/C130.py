N = int(input())

index_arr = []
m = 0
for i in range(N):
    a, b = input().split()
    if a == 'y' and b == 'y':
        continue

    index_arr.append(i+1)
    m += 1

print(m)
for index in index_arr:
    print(index)