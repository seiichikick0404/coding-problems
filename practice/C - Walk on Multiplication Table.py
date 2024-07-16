N = int(input())

# 最小移動回数を無限大で初期化
min_moves = float('inf') 

# Nの約数を探す
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        j = N // i
        # (i, j)が見つかった場合、i-1回の下移動とj-1回の右移動が必要
        moves = (i - 1) + (j - 1)
        min_moves = min(min_moves, moves)

print(min_moves)