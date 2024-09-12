# parent: 各園児が属してる列車の親のインデックスを持つ
# size: 各列車のサイズを配列で管理
# 上記は全てインデックスで園児の番号としてる


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 各園児の親を自身に初期化
        self.size = [1] * n  # 各列車のサイズを1に初期化

    def find(self, x):
        # 経路圧縮を使って親を見つける
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, winner, loser):
        root_winner = self.find(winner)
        root_loser = self.find(loser)

        if root_winner != root_loser:
            # 勝者の列車が親になるように統合
            self.parent[root_loser] = root_winner
            self.size[root_winner] += self.size[root_loser]

    def get_size(self, x):
        return self.size[self.find(x)]


# 標準入力の処理
n, m = map(int, input().split())
uf = UnionFind(n)

# ジャンケンの勝敗を反映
for _ in range(m):
    x, y = map(int, input().split())
    uf.union(x - 1, y - 1)  # 0-indexed に変換

# 各列車のサイズを確認し、最大のサイズを探す
max_size = 0
for i in range(n):
    max_size = max(max_size, uf.get_size(i))

# 最大の列車の先頭園児を見つける
winners = []
for i in range(n):
    if uf.get_size(i) == max_size and uf.find(i) == i:
        winners.append(i + 1)  # 1-indexed に戻す

# 結果を出力
winners.sort()
for winner in winners:
    print(winner)
