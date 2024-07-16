def is_collinear(p1, p2, p3):
    # 3点 (x1, y1), (x2, y2), (x3, y3) が同一直線上にあるかを判定する
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

N = int(input())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))
# print(coordinates)

collinear_count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 同一線上にあれば飛ばす
            if is_collinear(coordinates[i], coordinates[j], coordinates[k]):
                continue

            # 3点の面積が正の面積を持つ三角形か判定
            collinear_count += 1

print(collinear_count)
