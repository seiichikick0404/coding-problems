N, K = map(int, input().split())

hash_map = {}
for i in range(N):
    scores = list(map(int, input().split()))
    sum_score = sum(scores)
    hash_map[i+1] = sum_score

sorted_hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

ans = {}
for i in range(N):
    student, score = sorted_hash_map[i]
    if i + 1 <= K:
        ans[student] = 'Yes'
    else:
        # 上位K位のスコアを取得
        num, min_score = sorted_hash_map[K-1]
        if score + 300 >= min_score:
            ans[student] = 'Yes'
        else:
            ans[student] =  'No'


i = 1
while i < N + 1:
    print(ans[i])
    i += 1


