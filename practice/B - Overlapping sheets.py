





# 全てのシートが重なってる領域の面積を足す


n=int(input())
g=[[False for i in range(100)]for i in range(100)]
for k in range(n):
    a,b,c,d=map(int, input().split())
    for i in range(a,b):
        for j in range(c,d):
            g[i][j]=True
ans=0
for i in range(100):
    for j in range(100):
        if g[i][j]==True:
            ans+=1

print(g)
print(ans)



