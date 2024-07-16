N =  int(input())

hash_map = {}
str_list = []
for i in range(N):
    text = input()
    str_list.append(text)
    if hash_map.get(text) is None:
        hash_map[text] = 1
        print(text)
    else:
        print(f"{text}({hash_map[text]})")
        hash_map[text] += 1


