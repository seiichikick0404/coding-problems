# 2023 4/11 今回も動的計画法

# A = input()
# B = input()
# C = input()

# cards = {'A': list(A), 'B': list(C), 'C': list(C)}

# print(cards)

# # ゲームの開始（最初はAさんから）
# current_player = 'A'

# while True:
#     # 現在のプレイヤーがカードを持っている場合、先頭のカードを捨てる
#     if len(cards[current_player]) > 0:
#         discarded_card = cards[current_player].pop(0)
#         current_player = discarded_card.upper()
#     else:
#         # ゲームを終了
#         break


# print(current_player)


# 入力
SA=list(input())
SB=list(input())
SC=list(input())

# 次に捨てる人（初期値は'A')
x='a'

while True:
  if x=='a':
    # リストの要素が0ならば終了する
    if len(SA)==0:
      print('A')
      exit()

    # 先頭要素を除去してxに代入
    x=SA[0]
    SA.remove(x)
  elif x=='b':
    # リストの要素が0ならば終了する
    if len(SB)==0:
      print('B')
      exit()

    # 先頭要素を除去してxに代入
    x=SB[0]
    SB.remove(x)
  else:
    # リストの要素が0ならば終了する
    if len(SC)==0:
      print('C')
      exit()

    # 先頭要素を除去してxに代入
    x=SC[0]
    SC.remove(x)
