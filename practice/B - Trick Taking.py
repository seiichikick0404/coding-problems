

n, t = map(int, input().split())
colors = list(map(int, input().split()))
values = list(map(int, input().split()))

tmax = (-1, -1)  # [最大値, インデックス]
lmax = (-1, -1)  # [最大値, インデックス]

for i in range(n):
    if colors[i] == t:
        tmax = max(tmax, (values[i], i + 1))

    if colors[i] == colors[0]:
        lmax = max(lmax, (values[i], i + 1))

if tmax[0] != -1:
    print(tmax[1])
else:
    print(lmax[1])











# tmax = (-1, -1)  # (最大値, インデックス)
# lmax = (-1, -1)  # (最大値, インデックス)

# for i in range(n):
#     if c[i] == t:
#         tmax = max(tmax, (r[i], i + 1))  # インデックスを1ベースで保存
#     if c[i] == c[0]:
#         lmax = max(lmax, (r[i], i + 1))  # インデックスを1ベースで保存

# if tmax[0] != -1:
#     print(tmax[1])
# else:
#     print(lmax[1])



