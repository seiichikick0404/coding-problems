
S = input()

is_m = False
for s in S:
    if s == "M": 
        is_m = True
        continue

    if not is_m and s == "R":
        print('Yes')
        exit()

print('No')