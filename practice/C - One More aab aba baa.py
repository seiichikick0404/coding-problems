from itertools import permutations

def kth_permutation(s, k):
    # 文字列Sの全ての順列を生成
    perms = set(permutations(s))
    # 生成された順列を辞書順にソート
    sorted_perms = sorted(perms)
    # K番目の順列を取得（リストのインデックスは0から始まるので、K-1を使用）
    return ''.join(sorted_perms[k-1])


s, k = input().split()
k = int(k)

print(kth_permutation(s, k))