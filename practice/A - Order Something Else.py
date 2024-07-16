# 2023 7/22

# N = 料理の品数
# P = ドリンクの定価
# Q = 割引後のドリンク価格
# D = 料理の価格のリスト

N, P, Q = map(int, input().split())
DList = list(map(int, input().split()))

disCountTotal = min(DList) + Q

print(min([P, disCountTotal]))

