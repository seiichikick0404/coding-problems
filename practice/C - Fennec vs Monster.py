N, K = map(int, input().split())

monster_hp = list(map(int, input().split()))

monster_hp.sort(reverse=True)

# HPが高いモンスター順に必殺技で減らせるだけ減らす
monster_hp = monster_hp[K:]

# 残りのモンスターのHPの総数が答え
print(sum(monster_hp))
