N = int(input())
sizes = [tuple(map(int, input().split())) for _ in range(N)]

# 巨人たちを (B - A) の降順でソート
giants = sorted(sizes, key=lambda x: x[1] - x[0], reverse=True)

# 最初の巨人の頭の高さはそのまま
current_height = giants[0][1]

# 2番目以降の巨人を積み上げていく
for i in range(1, N):
    current_height += giants[i][0]

print(current_height)
