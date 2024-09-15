S_AB, S_AC, S_BC = input().split()

# 兄弟のリスト
brothers = ['A', 'B', 'C']

# 全ての年齢順の可能性を列挙（6通り）
from itertools import permutations
for order in permutations(brothers):
    # 各関係が与えられた条件を満たすか確認
    valid = True
    A_index = order.index('A')
    B_index = order.index('B')
    C_index = order.index('C')

    # AとBの関係
    if S_AB == '<':
        if A_index >= B_index:
            valid = False
    else:
        if A_index <= B_index:
            valid = False

    # AとCの関係
    if S_AC == '<':
        if A_index >= C_index:
            valid = False
    else:
        if A_index <= C_index:
            valid = False

    # BとCの関係
    if S_BC == '<':
        if B_index >= C_index:
            valid = False
    else:
        if B_index <= C_index:
            valid = False

    # 条件を全て満たす場合、次男を出力
    if valid:
        # 年齢順に並んでいるので、次男は中央の要素
        print(order[1])

