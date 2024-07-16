
N, Q = map(int, input().split())

hash_map = {}
for i in range(Q):
    event, target = map(int, input().split())

    if hash_map.get(target) is None:
        hash_map[target] = 0

    if event == 1:
        hash_map[target] += 1

    elif event == 2:
        hash_map[target] += 2
    else:
        # イベント3
        if hash_map[target] >= 2:
            print('Yes')
        else:
            print('No')
