
n, m, t = map(int, input().split())

move_power = list(map(int, input().split()))

bonus_map = {}
for i in range(m):
    index, power = map(int, input().split())
    bonus_map[index-1] = power


for i in range(n - 1):
    # 次に進めるかチェック
    if t - move_power[i] <= 0:
        print('No')
        exit()

    t -= move_power[i]

    # ボーナス部屋かチェック
    if bonus_map.get(i+1) is not None:
        t += bonus_map[i+1]

print('Yes')



