def find_winner(N, M, votes):
    # 各候補者の得票数を記録する辞書
    vote_counts = {i: 0 for i in range(1, N + 1)}
    current_winner = None
    max_votes = 0

    for i in range(M):
        # 票をカウント
        vote_counts[votes[i]] += 1

        # 現在の得票数
        current_votes = vote_counts[votes[i]]

        # 現在の候補者が最大得票数を更新するか、
        # 最大得票数が同じで候補者の番号がより小さい場合、当選者を更新
        if current_votes > max_votes or (current_votes == max_votes and votes[i] < current_winner):
            max_votes = current_votes
            current_winner = votes[i]

        # 当選者を出力
        print(current_winner)


N, M = map(int, input().split())
votes = list(map(int, input().split()))

find_winner(N, M, votes)

