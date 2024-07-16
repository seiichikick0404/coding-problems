N, K = map(int, input().split())
mod = 1000000007
if K == 1:
    print(1 if N == 1 else 0)
elif N == 1:
    print(K % mod)
elif N == 2:
    print(K * (K - 1) % mod)
else:
    # 直接 Python の組み込み関数 pow を使用してモジュラーべき乗を計算
    print(K * (K - 1) * pow(K - 2, N - 2, mod) % mod)
