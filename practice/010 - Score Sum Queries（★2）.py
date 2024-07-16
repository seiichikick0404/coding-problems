N = int(input())

cumulative_scores_1 = [0] * (N + 1)  # クラス1の得点の累積和
cumulative_scores_2 = [0] * (N + 1)  # クラス2の得点の累積和

for i in range(1, N + 1):
    c, p = map(int, input().split())
    if c == 1:
        cumulative_scores_1[i] = cumulative_scores_1[i - 1] + p
        cumulative_scores_2[i] = cumulative_scores_2[i - 1]
    else:
        cumulative_scores_2[i] = cumulative_scores_2[i - 1] + p
        cumulative_scores_1[i] = cumulative_scores_1[i - 1]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    class_first_score = cumulative_scores_1[R] - cumulative_scores_1[L - 1]
    class_second_score = cumulative_scores_2[R] - cumulative_scores_2[L - 1]
    print(class_first_score, class_second_score)

