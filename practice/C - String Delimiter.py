n = int(input())
l =  list(input())

start_flag = False
ans = ""
for val in l:
    if not start_flag and val == '"':
        start_flag = True
        ans += '"'
        continue

    # スタートしてるかつvalの値が「,」の場合「.」に変換
    if not start_flag and val == ",":
        ans += "."
        continue

    # スタートしてるかつvalが「"」の場合
    if start_flag and val == '"':
        start_flag = False
        ans += '"'
        continue

    ans += val

print(ans)

