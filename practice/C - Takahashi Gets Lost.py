# Read input values
h, w, n = map(int, input().split())
t = input()
s = [''] * (h + 1)

for i in range(1, h + 1):
    s[i] = input()

ans = 0

# Iterate over each cell in the grid
for i in range(1, h + 1):
    for j in range(w):
        if s[i][j] == '#':
            continue
        I, J = i, j
        ok = True
        # Follow the commands in t
        for c in t:
            if c == 'L':
                J -= 1
            elif c == 'R':
                J += 1
            elif c == 'U':
                I -= 1
            elif c == 'D':
                I += 1
            # Check if the new position is out of bounds or hits an obstacle
            if I < 1 or I > h or J < 0 or J >= w or s[I][J] == '#':
                ok = False
                break
        if ok:
            ans += 1

print(ans)
