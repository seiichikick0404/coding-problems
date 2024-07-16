n, m = map(int, input().split())

highs = list(map(int, input().split()))

ans = [True for _ in range(n)]

for i in range(m):
    p1, p2 = map(int, input().split())
    # ここで対象の値とつながる展望台の値を比較し、対象の展望台よりも高ければtrue
    if highs[p1-1] <=  highs[p2-1]:
        ans[p1-1] = False

    if highs[p2-1] <= highs[p1-1]:
        ans[p2-1] = False

count = sum()
print(count)

