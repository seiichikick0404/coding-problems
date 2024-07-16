

# 入力を受け取る
N, M = map(int, input().split())

# 全てのゲートの範囲を表すリスト
gates = [list(map(int, input().split())) for _ in range(M)]

# 全てのゲートが共通して受け入れるIDカードの範囲を見つける
max_L = max(gate[0] for gate in gates)
min_R = min(gate[1] for gate in gates)

# 共通範囲内のIDカードの数を計算
if max_L <= min_R:
    print(min_R - max_L + 1)
else:
    print(0)
