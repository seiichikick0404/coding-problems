N, Q = map(int, input().split())
T = list(map(int, input().split()))

# 抜いた歯を格納する配列
extracted = set()

for t in T:
    if t not in extracted:
        extracted.add(t)
    else:
        extracted.remove(t)


print(N - len(extracted))

