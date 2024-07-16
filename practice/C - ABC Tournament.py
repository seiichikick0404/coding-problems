def find_runner_up(N, rates):
    # 各選手の番号とレートをペアにしてリストを作成
    players = [(i + 1, rate) for i, rate in enumerate(rates)]

    # トーナメントを進行
    while len(players) > 2:
        next_round = []
        for i in range(0, len(players), 2):
            # 隣り合う選手同士で対戦し、レートが高い方が次のラウンドへ
            if players[i][1] > players[i+1][1]:
                next_round.append(players[i])
            else:
                next_round.append(players[i+1])
        players = next_round

    # 最後のラウンドで敗れる選手（準優勝者）を決定
    if players[0][1] > players[1][1]:
        return players[1][0]  # 選手の番号を返す
    else:
        return players[0][0]

N = int(input())
l = list(map(int, input().split()))

print(find_runner_up(N, l))



