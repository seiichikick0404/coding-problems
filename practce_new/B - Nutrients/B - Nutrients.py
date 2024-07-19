
# N:食品数、M:栄養素数
N, M = map(int, input().split())

# A: Ai番目の目標栄養素数
A = list(map(int, input().split()))

# 食品の栄養素データを読み込む
eat_records = []
for i in range(N):
    eat_records.append(list(map(int, input().split())))

# 栄養素ごとの現在の摂取量を初期化
current_intake = [0] * M

# 各食品の栄養素を累積
for i in range(N):
    for j in range(M):
        current_intake[j] += eat_records[i][j]

# 目標を達成しているか確認
achieved = True
for i in range(M):
    if current_intake[i] < A[i]:
        achieved = False
        break

# 結果を出力
if achieved:
    print('Yes')
else:
    print('No')





