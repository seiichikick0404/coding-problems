# 標準入力の値を受け取る
import sys
input = sys.stdin.read

def count_bingo(N, K, bingo_card, drawn_numbers):
    # ビンゴカード上の番号の位置を辞書で保存
    number_position = {}
    for i in range(N):
        for j in range(N):
            number_position[bingo_card[i][j]] = (i, j)
    
    # ビンゴのカウント用
    row_count = [0] * N
    col_count = [0] * N
    diag1_count = 0
    diag2_count = 0
    
    # 中央のマス(0)は最初から開けるのでカウントしておく
    center = N // 2
    row_count[center] += 1
    col_count[center] += 1
    diag1_count += 1
    diag2_count += 1
    
    # 抽選された数字に基づいてカウントを更新
    for number in drawn_numbers:
        if number in number_position:
            i, j = number_position[number]
            row_count[i] += 1
            col_count[j] += 1
            if i == j:
                diag1_count += 1
            if i + j == N - 1:
                diag2_count += 1
    
    # ビンゴが成立しているか確認
    bingo_count = 0
    for i in range(N):
        if row_count[i] == N:
            bingo_count += 1
        if col_count[i] == N:
            bingo_count += 1
    if diag1_count == N:
        bingo_count += 1
    if diag2_count == N:
        bingo_count += 1
    
    return bingo_count

def main():
    # 入力をすべて読み込む
    data = input().splitlines()
    
    # 1行目のN, Kを取得
    N, K = map(int, data[0].split())
    
    # 次のN行のビンゴカードの数字を取得
    bingo_card = []
    for i in range(1, N+1):
        bingo_card.append(list(map(int, data[i].split())))
    
    # 最後の行の抽選された数字を取得
    drawn_numbers = list(map(int, data[N+1].split()))
    
    # ビンゴの数を数えて出力
    result = count_bingo(N, K, bingo_card, drawn_numbers)
    print(result)

# メイン関数を実行
if __name__ == "__main__":
    main()
