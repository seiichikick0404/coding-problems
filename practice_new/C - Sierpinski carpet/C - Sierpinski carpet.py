def generate_carpet(N):
    # ベースケース：レベル0は # のみ
    if N == 0:
        return ["#"]

    # レベル N-1 のカーペットを再帰的に生成
    smaller_carpet = generate_carpet(N - 1)
    size = len(smaller_carpet)
    new_size = size * 3
    new_carpet = []

    # レベル N のカーペットを生成する
    for i in range(new_size):
        if size <= i < 2 * size:
            # 中央のブロックには白いマスを入れる
            new_carpet.append(smaller_carpet[i % size] + '.' * size + smaller_carpet[i % size])
        else:
            # 上と下のブロックには前のレベルのカーペットを3つ並べる
            new_carpet.append(smaller_carpet[i % size] * 3)

    return new_carpet

# 入力の受け取り
N = int(input())

# カーペットを生成
carpet = generate_carpet(N)

# 出力
for row in carpet:
    print(row)
