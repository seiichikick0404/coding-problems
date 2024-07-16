H, W = map(int, input().split())

gridA = []
for i in range(H):
    gridA.append(list(input()))

gridB = []
for i in range(H):
    gridB.append(list(input()))

def check_match(s, t):
    for i in range(H):
        for j in range(W):
            # シフト後の新しいポジションを計算する
            new_i = (i - s) % H
            new_j = (j - t) % W
            # Aの新しい位置の文字がBの文字と一致するかチェックする。
            if gridA[new_i][new_j] != gridB[i][j]:
                return False
    return True

# sとtのすべての可能な組み合わせを試す
for s in range(H):
    for t in range(W):
        if check_match(s, t):
            print("Yes")
            exit(0)

print("No")
