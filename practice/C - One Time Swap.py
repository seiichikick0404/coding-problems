from collections import Counter
S=input()
N=len(S)
count=Counter(S)
ans=(N*N-sum(x*x for x in count.values()))//2
if max(count.values())>1:
  ans+=1
print(ans)