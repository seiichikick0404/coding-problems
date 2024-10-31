
ans = 0
for i in range(1, 13):
    text = input()
    if len(text) == i:
        ans += 1

print(ans)