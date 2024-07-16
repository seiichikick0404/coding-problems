

def is_ok(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True



N = int(input())

l = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j: continue

        if i != j and is_ok(l[i] + l[j]):
            print('Yes')
            exit()

print('No')