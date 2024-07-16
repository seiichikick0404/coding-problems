from itertools import permutations

def count_paths_matching_time(N, K, T):
    # 全ての都市のインデックスのリストを生成（0から始まるため、1を引く）
    cities = list(range(N))

    # 都市1を起点とするため、リストから除外
    cities.remove(0)

    # 合計移動時間がKになる経路の数を数える
    count = 0
    for perm in permutations(cities):
        # 都市1からスタートして最初の都市への移動時間を加える
        time = T[0][perm[0]]

        # 順列内の各都市間を移動する時間を加算
        for i in range(len(perm) - 1):
            time += T[perm[i]][perm[i + 1]]
        
        # 最後の都市から都市1へ戻る時間を加える
        time += T[perm[-1]][0]
        
        # 合計時間がKに一致するかチェック
        if time == K:
            count += 1
            
    return count



N, K = map(int, input().split())

T = []
for _ in range(N):
    city = list(map(int, input().split()))
    T.append(city)



print(count_paths_matching_time(N, K, T))
