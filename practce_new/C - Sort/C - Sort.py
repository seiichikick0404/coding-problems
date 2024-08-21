N = int(input())
A = list(map(int, input().split()))

# 位置を管理するための配列を作成する
position = [0] * (N + 1)
for i in range(N):
    position[A[i]] = i

operations = []

# 1 から N まで順番に正しい位置にする
for i in range(N):
    if A[i] != i + 1:
        correct_index = position[i + 1]
        
        # i 番目と correct_index 番目を入れ替える
        A[i], A[correct_index] = A[correct_index], A[i]
        
        # スワップしたので位置も更新する
        position[A[correct_index]] = correct_index
        position[A[i]] = i
        
        # 操作を記録
        operations.append((i + 1, correct_index + 1))

# 結果を出力
print(len(operations))
for op in operations:
    print(op[0], op[1])
