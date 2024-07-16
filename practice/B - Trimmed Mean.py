
N = int(input())
scores = list(map(int, input().split()))

scores.sort()

# 最高点と最低点を排除
i = 0
while i < N:
    scores.pop(-1)
    scores.pop(0)
    i += 1

# 平均点を計算
print(sum(scores) / len(scores))