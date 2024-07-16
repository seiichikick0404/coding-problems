


def check_all_pairs_participated(N, M, dances):
    participated_pairs = set()
    for dance in dances:
        for i in range(len(dance)):
            for j in range(i + 1, len(dance)):
                pair = (dance[i], dance[j])
                participated_pairs.add(pair)

    all_pairs = set()
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            all_pairs.add((i, j))

    print(participated_pairs)
    print(all_pairs)

    return "Yes" if all_pairs.issubset(participated_pairs) else "No"


N, M = map(int, input().split())
dances = []
for _ in range(M):
    k, *participants = map(int, input().split())
    dances.append(participants)

result = check_all_pairs_participated(N, M, dances)
print(result)


