
N = int(input())
count = 0
for _ in range(N):
    s = input()
    if count == 2:
        print('No')
        exit()

    if s == "sweet":
        count += 1
    else:
        count = 0

print('Yes')
