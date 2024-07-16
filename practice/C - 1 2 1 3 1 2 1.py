def create_sequence(n):
    if n == 1:
        return "1"
    else:
        prev_seq = create_sequence(n - 1)
        return prev_seq + " " + str(n) + " " + prev_seq

N = int(input())
result = create_sequence(N)
print(result)
