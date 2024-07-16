def solve(S):
    # 2進数で全探索
    for msk in range(1 << 3):
        sm = int(S[0])
        expression = S[0]
        for i in range(3):
            if msk & (1 << i):
                sm += int(S[i + 1])
                expression += "+"
            else:
                sm -= int(S[i + 1])
                expression += "-"
            expression += S[i + 1]
        if sm == 7:
            expression += "=7"
            return expression

# テスト実行
S = input()  # 例: '1222'
print(solve(S))
