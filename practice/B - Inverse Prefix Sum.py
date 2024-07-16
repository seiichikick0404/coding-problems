
N = int(input())
l = list(map(int, input().split()))

ans = []
ans.append(l[0])
for i in range(1, N):
    num = l[i] - sum(ans)
    ans.append(num)

    
print(*ans)
    


