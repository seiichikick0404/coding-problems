# 入力の読み取り
N, M = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append([0] + row)  # 1-based indexing のため、先頭にダミーを追加

X = int(input())

moves = []
for _ in range(X):
    R, S = map(int, input().split())
    moves.append((R, S))

# 初期状態
current_station = 1  # 駅番号
total_fare = 0

for R, S in moves:
    # 現在の駅から移動先駅 S への運賃を計算
    fare = abs(A[R - 1][S] - A[R - 1][current_station])
    total_fare += fare
    # 現在の駅番号を更新
    current_station = S

# 結果を出力
print(total_fare)