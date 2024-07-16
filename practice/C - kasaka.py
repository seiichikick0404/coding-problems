S = input()

for _ in range(10*6):
    if S == S[::-1]:
        print('Yes')
        exit()

    S = "a" + S

print('No')