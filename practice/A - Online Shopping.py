
n , s, k = map(int, input().split())


total = 0
for i in range(n):
    price, purchase_num = map(int, input().split())
    total += price * purchase_num

if total >= s:
    print(total)
else:
    print(total + k)
