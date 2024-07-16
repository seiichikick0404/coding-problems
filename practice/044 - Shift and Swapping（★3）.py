N, Q = map(int, input().split())
A = list(map(int, input().split()))

shift_count = 0  # シフトの回数を追跡

for _ in range(Q):
    T, X, Y = map(int, input().split())
    if T == 1:
        # インデックスをシフト分調整してから入れ替え
        A[(X-1-shift_count)%N], A[(Y-1-shift_count)%N] = A[(Y-1-shift_count)%N], A[(X-1-shift_count)%N]
    elif T == 2:
        # シフトの回数を1増やす
        shift_count += 1
    else:
        # インデックスをシフト分調整してから値を出力
        print(A[(X-1-shift_count)%N])
