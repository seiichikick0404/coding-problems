N, K = map(int, input().split())
remainder = N % K
difference = K - remainder
min_value = min(remainder, difference)
print(min_value)