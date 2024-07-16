N = int(input())
nums = list(map(int, input().split()))

# 1からNまでの各数値の出現回数をカウント
count = [0] * (N + 1)
for num in nums:
    if 1 <= num <= N:
        count[num] += 1

# 連番部分列の最長の長さを求める
max_seq_length = 0
for i in range(1, N + 1):
    if count[i] == 0:
        break
    max_seq_length += 1

# 必要な削除回数を計算
delete_count = N - max_seq_length

# 出力
print(delete_count)
