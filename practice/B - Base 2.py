l = list(map(int, input().split()))

sum = 0
for i in range(len(l)):
    sum += l[i] * (2 ** i)

print(sum)
