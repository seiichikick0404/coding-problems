

k, g, m = map(int, input().split())

x, y = 0,0
for i in range(k):
    if x == g:
      x = 0
    elif y == 0:
      y = m
    else:
      z = min(y,g-x)
      x, y = x + z, y - z
print(str(x)+" "+str(y))