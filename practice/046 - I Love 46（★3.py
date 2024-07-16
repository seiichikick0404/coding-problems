

from collections import Counter

def count_combinations(N, A, B, C):
    # 46で割った余りのカウント
    mod_counts_A = Counter([a % 46 for a in A])
    mod_counts_B = Counter([b % 46 for b in B])
    mod_counts_C = Counter([c % 46 for c in C])

    # 組み合わせの総数を計算
    total_combinations = 0
    for a_remainder, a_count in mod_counts_A.items():
        for b_remainder, b_count in mod_counts_B.items():
            # Cのリストから補完する必要のある余りを計算
            c_remainder_needed = (46 - (a_remainder + b_remainder) % 46) % 46
            c_count = mod_counts_C.get(c_remainder_needed, 0)
            # 組み合わせに応じてカウントを加算
            total_combinations += a_count * b_count * c_count

    return total_combinations


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

print(count_combinations(N, A, B, C))