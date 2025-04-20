""" 入力を受け取る """
N, M, K = map(int, input().split())
C, A, R = [],[],[]
for _ in range(M):
    c, *a, r = input().split()
    C.append(int(c))
    A.append([int(i) - 1 for i in a])
    R.append(r)

""" 鍵の組み合わせを bit全探索 """
ans = 0
for mask in range(1 << N):
    ok = True
    for i in range(M):
        cnt = 0
        for a in A[i]:
            if (mask >> a) & 1 == 1:
                cnt += 1
        if R[i] == 'o' and cnt < K:
            ok = False
        if R[i] == 'x' and cnt >= K:
            ok = False
    if ok:
        ans += 1
print(ans)