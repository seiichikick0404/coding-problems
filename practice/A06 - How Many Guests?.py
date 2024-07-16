
# 開催日、質問数
N, Q = map(int, input().split())

# 来場者配列
peopleList = list(map(int, input().split()))

# 累積和の配列作成
cumulativeSumList = [0]
for i in range(N):
    cumulativeSumList.append(cumulativeSumList[i] + peopleList[i])

# 各クエリに対応
for _ in range(Q):
    start, end = map(int, input().split())
    print(cumulativeSumList[end] - cumulativeSumList[start - 1])