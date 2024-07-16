
N, M = map(int, input().split())

S = input()

muji_ok=M  # 無地/洗濯済み
muji_ng=0  # 無地/着用済み
logo_ok=0  # ロゴ/洗濯済み
logo_ng=0  # ロゴ/着用済み
for c in S:
  if c=='0':
    # 洗濯をし、全てのngがokになる
    muji_ok+=muji_ng
    muji_ng=0
    logo_ok+=logo_ng
    logo_ng=0
  elif c=='1':
    if muji_ok:
      # 無地のTシャツがあるなら着る
      muji_ok-=1
      muji_ng+=1
    elif logo_ok:
      # ロゴ入りのTシャツがあるなら着る
      logo_ok-=1
      logo_ng+=1
    else:
      # 着るものがないならロゴ入りのTシャツを買って着る
      logo_ng+=1
  elif c=='2':
    if logo_ok:
      # ロゴ入りのTシャツがあるなら着る
      logo_ok-=1
      logo_ng+=1
    else:
      # 着るものがないならロゴ入りのTシャツを買って着る
      logo_ng+=1

    
print(logo_ok+logo_ng)
