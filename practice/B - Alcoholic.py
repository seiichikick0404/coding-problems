N, X = map(int, input().split())

s = 0
for i in range(N):
  v,p = map(int,input().split())
  s += v*p
  if s > X*100:
    print(i+1)
    exit()
print(-1)


