N, M = map(int, input().split())

hash_map = {}
for _ in range(M):
    q, result = input().split()
    q = int(q)
    if hash_map.get(q):
        hash_map[q].append(result)
    else:
        hash_map[q] = [result]

ac_count = 0
wa_count =0
for q, results in hash_map.items():
    # ACが存在するかチェック
    tmp_results = results.copy()
    tmp_results = set(tmp_results)
    if "AC" in tmp_results:
        ac_count += 1

    # resultsの中から最初のAC位置を見つける
    if "AC" in tmp_results and "WA" in tmp_results:
        wa_count += results.index('AC')

print(ac_count, wa_count)

