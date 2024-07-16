# バッテリー容量N, カフェに行った回数M, 帰宅時刻T
N, M, T = map(int, input().split())
N_max = N

prev_time = 0
for i in range(M):
    A, B = map(int, input().split())

    # 経過時間
    elapsed_time = abs(prev_time - A)

    # カフェ滞在開始時の残量
    N -= elapsed_time

    if N <= 0:
        print('No')
        exit()

    # 充電後のバッテリーを反映
    N += B - A
    # バッテリー容量を超えないように調整
    if N > N_max:
        N = N_max

    prev_time = B

# 最後のカフェから帰宅までのバッテリー消費量を計算
N -= abs(T - prev_time)

if N <= 0:
    print('No')
else:
    print('Yes')
