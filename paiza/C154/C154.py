N, L = map(int, input().split())

prices = list(map(int, input().split()))
prices.sort()

max_price = prices[-1]
total = 0
for i in range(N):
    if prices[i] >= L and i+1 == N:
      total += prices[i] // 2
    else:
      total += prices[i]

print(total)
