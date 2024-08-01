import sys

S, T = input().split()

for w in range(1, len(S)):
    for c in range(1, w+1):
        result = ""
        for i in range(0, len(S), w):
            if i + c - 1 < len(S):
                result += S[i + c - 1]
        if result == T:
            print('Yes')
            sys.exit()
print('No')

