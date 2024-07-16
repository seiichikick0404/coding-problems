n = input()
l = list(map(int, input().split()))

l.sort(reverse=True)

result = 0
for i in range(0,len(l)):
    if (i % 2 == 0): result += l[i]
    elif (i % 2 >= 1): result -= l[i]
    else: result += l[i]

print(result)
