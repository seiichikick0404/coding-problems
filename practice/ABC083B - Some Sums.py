n,a,b = map(int,input().split())

n = 20
a = 2
b = 5
total = 0

for i in range(n):
    j = i+1
    lst = []
    while j > 0:
        lst.append(j%10)
        j //= 10
    total = total+i+1 if a<=sum(lst)<=b else total

print(total)
