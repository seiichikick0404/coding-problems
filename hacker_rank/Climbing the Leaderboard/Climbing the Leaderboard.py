

def binary_search(ranked_list, target):
    start = 0
    end = len(ranked_list) - 1
    while start <= end:
        mid = (start + end) // 2

        if ranked_list[mid] < target:  # 降順なので逆
            end = mid - 1
        elif ranked_list[mid] > target:
            start = mid + 1
        else:
            return mid
    return start

def climbingLeaderboard(ranked, player):
    # リーダーボードのスコアを一意にして降順にソート
    ranked_list = sorted(set(ranked), reverse=True)
    ans = []

    for score in player:
        # ターゲットスコアのランクインデックスを取得
        rank_index = binary_search(ranked_list, score)
        # ランクはインデックス+1
        ans.append(rank_index + 1)

    return ans

# テストケース
ranked = [100, 90, 90, 80]
player = [70, 80, 105]
result = climbingLeaderboard(ranked, player)
print(result)  # 出力: [4, 3, 1]






ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
result = climbingLeaderboard(ranked, player)
print(result)