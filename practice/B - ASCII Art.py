
H, W = map(int, input().split())

for _ in range(H):
    row = list(map(int, input().split()))
    output = []

    for num in row:
        if num == 0:
            output.append('.')
        else:
            output.append(chr(num + 64))

    print("".join(output))




