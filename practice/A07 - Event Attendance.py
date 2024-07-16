# 入力を受け取る
D = int(input().strip())
N = int(input().strip())

# いもす法の配列を初期化
imos_array = [0] * (D + 1)

# いもす法の準備
for _ in range(N):
    L, R = map(int, input().split())
    imos_array[L - 1] += 1  # 出席開始日に1を加える
    imos_array[R] -= 1     # 出席終了日の次の日に-1を加える


# 累積和の計算
for i in range(1, D):
    imos_array[i] += imos_array[i - 1]

# 結果の出力
for i in range(D):
    print(imos_array[i])


