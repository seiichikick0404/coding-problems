def lineup(N, A):
    # リンクドリストを作成
    # key: 人の番号, value: その人の後ろに並ぶべき人の番号
    next_person = {}
    head = None  # リストの先頭を表す変数

    for i, a in enumerate(A):
        if a == -1:
            head = i + 1  # 先頭の人を設定（1-indexed）
        else:
            next_person[a] = i + 1

    # リンクドリストを走査して、並び順を復元
    order = []
    current = head
    while current:
        order.append(current)
        current = next_person.get(current)  # 次の人を取得

    return order

N = int(input())
A = list(map(int, input().split()))

print(*lineup(N, A))
