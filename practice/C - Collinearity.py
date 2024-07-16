
def is_collinear(p1, p2, p3):
    # 3点 (x1, y1), (x2, y2), (x3, y3) が同一直線上にあるかを判定する
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) == 0


N = int(input())

coordinates = []
for i in range(N):
    x, y = map(int, (input().split()))
    coordinates.append((x, y))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if is_collinear(coordinates[i], coordinates[j], coordinates[k]):
                print("Yes")
                exit()

print('No')








