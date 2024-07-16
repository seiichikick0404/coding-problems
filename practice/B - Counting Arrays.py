N = int(input())

set_pair = set()
for i in range(N):
    set_pair.add(tuple(map(int, input().split())))

print(len(set_pair))