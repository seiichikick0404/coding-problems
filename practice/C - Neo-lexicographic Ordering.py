def neo_lexicographic_ordering(X, S):
    # 新しいアルファベット順序に基づいて各文字の位置をマッピング
    pos = {char: i for i, char in enumerate(X)}

    # 新しいアルファベット順序に基づいて文字列をソート
    S.sort(key=lambda s: [pos[char] for char in s])

    return S

# 入力例
X = input()
N = int(input())
S = [input() for _ in range(N)]

# ソートされた結果を出力
for s in neo_lexicographic_ordering(X, S):
    print(s)