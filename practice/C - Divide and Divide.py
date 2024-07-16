import math

# 黒板にnがある
# ①黒板から2以上のnを選んでnを消す
# ②n円を支払う
# ③n / 2の切り下げ値と切り上げ値を黒板に追加
# ①に戻る。 存在しない場合は処理終了でその時点での支払い金額を表示

N = int(input())
curr_list = set([N])
total = 0

while True:
    # curr_list内に2以上の値があるかチェック
    if len(curr_list) == 1 and 1 in curr_list:
        break

    # curr_listに1が含まれてる場合削除
    tmp_set = curr_list.copy()
    if 1 in curr_list:
        tmp_set.remove(1)

    # 黒板から2以上のnを選ぶ
    tmp_list = list(tmp_set)
    target = tmp_list[0]

    # nをcurr_listから削除
    curr_list.remove(target)

    # n円支払う
    total += target

    # n / 2の切り下げ値と切り上げ値を黒板に追加
    A_ceil = math.ceil(target / 2)
    B_floor = math.floor(target / 2)
    curr_list.add(A_ceil)
    curr_list.add(B_floor)

print(total)
