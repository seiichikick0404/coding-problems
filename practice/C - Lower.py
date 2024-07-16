N = int(input())
l = list(map(int, input().split()))

max_count = 0
count = 0
for i in range(N-1):
    if l[i] >= l[i+1]:
        # 現在のマスの高さが右隣のマスの高さ以下なら、移動回数をカウントアップ
        count += 1
        max_count = max(max_count, count)
    else:
        # 右隣のマスの高さが現在居るマスの高さより高い場合、カウントをリセット
        count = 0

print(max_count)