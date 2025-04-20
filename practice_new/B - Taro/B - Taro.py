N, M = map(int, input().split())

families = {}  # 家族ごとに子供の性別を順番に保存するディクショナリ

for _ in range(M):
    fam, sex = input().split()
    fam_index = int(fam)

    # 家族が初めて出てきた場合、空のリストを作成
    if fam_index not in families:
        families[fam_index] = []

    # 現在の子供を家族のリストに追加
    families[fam_index].append(sex)

    # 判定
    if sex == 'M':
        # この子より前に男性がいない場合は長男
        if families[fam_index].count('M') == 1:
            print('Yes')
        else:
            print('No')
    else:
        # 女性の場合は常に 'No'
        print('No')


