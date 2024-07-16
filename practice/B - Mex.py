# 入力
n = int(input())
a = list(map(int, input().split()))

# 数列 a に含まれない最小の非負整数を探す
a_set = set(a)  # 検索効率を向上させるためセットに変換
for ans in range(n + 1):  # ans が n までではなく、n+1 まで必要
    if ans not in a_set:
        print(ans)
        break







