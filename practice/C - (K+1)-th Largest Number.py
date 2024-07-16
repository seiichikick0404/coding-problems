n = int(input())
mp = {}

for _ in range(n):
    a = int(input())
    if a in mp:
        mp[a] += 1
    else:
        mp[a] = 1

for key in sorted(mp, reverse=True):
    print(mp[key])

for _ in range(n - len(mp)):
    print(0)
