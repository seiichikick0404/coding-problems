tiles = list(input())

A = []
B = []
for i in range(1, len(tiles)+1):
        if i % 2 == 0:
            A.append("0")
            B.append("1")
        else:
            A.append("1")
            B.append("0")

A_count = 0
B_count = 0
for i in range(len(tiles)):
    if tiles[i] != A[i]:
         A_count += 1

    if  tiles[i] != B[i]:
         B_count += 1

print(min(A_count, B_count))