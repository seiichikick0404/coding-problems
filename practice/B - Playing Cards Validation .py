

n = int(input())

duplicate = []

for i in range(n):
    s = input()
    if s in duplicate:
        print('No')
        exit()

    if s[0] not in ['H', 'D', 'C', 'S'] or s[1] not in [ 'A' , '2' , '3' , '4','5','6','7','8','9','T','J', 'Q', 'K']:
        print('No')
        exit()

    duplicate.append(s)


print('Yes')