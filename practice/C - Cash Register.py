S = input()

count = 0

while S:
    if S[-1] == '0' and len(S) > 1 and S[-2] == '0':
        S = S[:-2]
    else:
        S = S[:-1]
    
    count += 1

print(count)