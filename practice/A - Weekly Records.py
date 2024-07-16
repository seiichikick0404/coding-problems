N = int(input().strip())

stepList = list(map(int, input().split()))


# 累積和の配列にする
cumulativeList = [0]
for i in range(len(stepList)):
    cumulativeList.append(cumulativeList[i] + stepList[i])

start, end = 1, 7
# 累積和を使い、計算
for j in range(N):
    print(cumulativeList[end] - cumulativeList[start - 1])
    start += 7
    end += 7