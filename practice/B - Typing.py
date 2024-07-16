S = input().strip()  # 正しい文字列
T = input().strip()  # 間違った文字列

output = []
t_index = 0

for s_char in S:
    while t_index < len(T):
        if s_char == T[t_index]:
            output.append(t_index + 1)
            t_index += 1
            break
        t_index += 1

print(*output)
