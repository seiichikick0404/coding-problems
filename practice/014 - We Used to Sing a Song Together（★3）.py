N = int(input())
houses = list(map(int, input().split()))
schools = list(map(int, input().split()))

# 小学生の家と小学校の位置をそれぞれソート
houses.sort()
schools.sort()

# 位置の差の絶対値の合計を計算
total = 0
for i in range(N):
    total += abs(houses[i] - schools[i])
    
print(total)

