# 入力を受け取る
h, w = map(int, input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]

# A. 各行の文字列を列ごとに分割
Ts, Tt = ['' for _ in range(w)], ['' for _ in range(w)]
for i in range(h):
    for j in range(w):
        Ts[j] += s[i][j]
        Tt[j] += t[i][j]

# B. 列をソート
Ts.sort()
Tt.sort()

# 結果の出力
if Ts == Tt:
    print("Yes")
else:
    print("No")






