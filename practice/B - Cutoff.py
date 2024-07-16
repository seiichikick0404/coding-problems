# N,X = map(int,input().split())
# A = list(map(int,input().split()))

# for finalScore in range(0,101):
#     B = A.copy()
#     B.append(finalScore)
#     B.sort()

#     # 先頭と末尾以外の値の合計値を計算
#     sum = 0
#     for i in range(1,N-1):
#         sum += B[i]

#     if sum >= X:
#         print(finalScore)
#         exit()
# print("-1")


# 練習問題
N, X = map(int, input().split())
scores = list(map(int, input().split()))

for finalScore in range(0, 101):
    scoresCopy = scores.copy()
    scoresCopy.append(finalScore)
    scoresCopy.sort()

    # 先頭と末尾を抜いたスコアの合計を計算
    sum = 0
    for i in range(1, N-1):
        sum += scoresCopy[i]

    if sum >= X:
        print(finalScore)
        exit()

print("-1")