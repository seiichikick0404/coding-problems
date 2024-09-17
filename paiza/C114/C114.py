N = int(input())

# すべての文字列を最初にリストに格納
strings = [input() for _ in range(N)]

prev_end = None

# すべての文字列に対してロジックを実行
for curr_str in strings:
    curr_start = curr_str[0]
    curr_end = curr_str[-1]
    if prev_end is None:
        prev_end = curr_end
    elif prev_end != curr_start:
        ans = [prev_end, curr_start]
        print(*ans)
        exit()
    else:
        prev_end = curr_end

print('Yes')


