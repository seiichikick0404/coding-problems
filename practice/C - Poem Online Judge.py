N = int(input())
original_map = {}
for i in range(N):
    text, score = input().split()
    score = int(score)
    if original_map.get(text) is None:
        original_map[text] = (i, score)

# 得点が高い順にソートし、得点が同じ場合は順番が小さい方を選ぶ
sorted_data = sorted(original_map.items(), key=lambda x: (x[1][1], -x[1][0]), reverse=True)

# 最高点の順番を取得
highest_score_order = sorted_data[0][1][0]

print(highest_score_order + 1)

