N, W = map(int, input().split())

unit_weights = []

for i in range(N):
    a, b = map(int, input().split())
    unit_weights.append((a, b))

unit_weights.sort(reverse=True)

res = 0
for deliciousness, amount in unit_weights:
    used = min(W, amount)
    res += deliciousness * used
    W -= used

print(res)
