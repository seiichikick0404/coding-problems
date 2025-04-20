spaces = [list(input()) for _ in range(8)]

def search_col(curr, spaces):
    for i in range(8):
        if spaces[i][curr[1]] == "#":
            return False
    return True


ans = 0
for i in range(8):
    row = set(spaces[i])
    if "#" in row: continue

    for j in range(8):
        if search_col((i, j), spaces):
            ans += 1

print(ans)
