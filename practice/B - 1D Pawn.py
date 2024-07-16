def move_pieces(N, K, Q, A, L):
    # コマの位置を初期化
    positions = A[:]

    # Q回の操作を実行
    for l in L:
        l -= 1  # 0-indexedに調整
        if positions[l] == N:
            continue  # すでに一番右にある場合はスキップ
        if l < K-1 and positions[l] + 1 == positions[l+1]:
            continue  # 右隣にコマがある場合はスキップ
        positions[l] += 1  # コマを右に移動

    return positions

# 入力例
N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

# コマの最終的な位置を計算
final_positions = move_pieces(N, K, Q, A, L)

# 結果の出力
print(*final_positions)


