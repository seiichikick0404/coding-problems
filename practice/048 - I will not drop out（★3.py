def max_score(N, K, problems):
    vec = []
    for A, B in problems:
        vec.append(B)
        vec.append(A - B)

    # 答えを求める
    Answer = 0
    vec.sort(reverse=True)
    for i in range(K):
        Answer += vec[i]

    return Answer




N, K = map(int, input().split())

problems = []
for i in range(N):
    # 満点、部分点 -> 部分点は満点より小さく、満点の半分より大きい
    A, B = map(int, input().split())
    problems.append((A, B))

print(max_score(N, K, problems))









