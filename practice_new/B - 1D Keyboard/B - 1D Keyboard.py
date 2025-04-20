target_keys = list(input())
base_keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ans = 0
for i in range(25):
    start = target_keys.index(base_keys[i])
    end = target_keys.index(base_keys[i+1])
    diff = abs(start - end)
    ans += diff

print(ans)



