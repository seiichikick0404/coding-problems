# くじ引き
# N 引いた回数
# A 引いた結果 -> 1はアタリ、0はハズレ
# L回~R回目
# Q 質問

# L ~ R回目のの中でアタリとハズレどっちが多い？という質問がQ個与えられるのでそれに答える


N = int(input())
resultList = list(map(int, input().split()))
Q = int(input())

# 累積和の配列を計算します
cumulative_sums = [0]
for i in range(N):
    cumulative_sums.append(cumulative_sums[i] + resultList[i])


for _ in range(Q):
    start, end = map(int, input().split())
    # start-1からendまでの和を計算します
    win = cumulative_sums[end] - cumulative_sums[start-1]
    # ハズレの数は全体の数からアタリの数を引くことで得られます
    lose = (end - start + 1) - win
    # 判定します
    if win > lose:
        print("win")
    elif lose > win:
        print("lose")
    else:
        print("draw")