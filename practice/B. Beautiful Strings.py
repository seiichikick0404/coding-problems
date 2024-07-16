# 2023 4/7
W = input()

hashMap = {}

for i in range(len(W)):
    hashMap[W[i]] = 0

for i in range(len(W)):
    if 97 <= ord(W[i]) <= 122:
        hashMap[W[i]] += 1


for value in hashMap.values():
    if value % 2 != 0:
        print("No")
        exit()

print("Yes")