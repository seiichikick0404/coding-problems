def ekiden_converter(N, A, M, rumors):
    # 仲が悪い選手間の制約を初期化
    kenaku = [[False] * (N + 1) for _ in range(N + 1)]
    for x, y in rumors:
        kenaku[x][y] = True
        kenaku[y][x] = True

    # 選手のリストを初期化
    vec = [i for i in range(1, N + 1)]
    
    # 答えの初期値を設定（非常に大きな値）
    Answer = float('inf')
    
    # 全探索
    from itertools import permutations
    for perm in permutations(vec):
        flag = True
        sum = 0
        for i in range(N - 1):
            if kenaku[perm[i]][perm[i + 1]]:
                flag = False
                break
        if flag:
            for i in range(N):
                sum += A[perm[i] - 1][i]
            Answer = min(Answer, sum)
    
    # 答えが更新されていなければ -1 を返す
    if Answer == float('inf'):
        Answer = -1
    return Answer


N = int(input)
A = []
for i in range(N):
    l = list(map(int, input().split()))
    A.append(l)

M = int(input())
rumors = []
for i in range(M):
    tuple = tuple(map(int, input().split()))
    rumors.append(tuple)

print(ekiden_converter(N, A, M, rumors))

