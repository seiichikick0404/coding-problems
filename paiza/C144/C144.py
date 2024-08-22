N = int(input())

hash_map = {
    'G': 'P',
    'C': 'G',
    'P': 'C'
}

count = 0
for _ in range(N):
    A, B = input().split()

    if hash_map[B] == A:
        count += 1

print(count)