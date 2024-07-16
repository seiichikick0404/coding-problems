def find_max_dango_level(S):
    N = len(S)
    ans = 0

    # 文字列Sを2回走査（元の順序と反転した順序）
    for flip in range(2):
        level = 0
        for i in range(N):
            if S[i] == '-':
                ans = max(ans, level)
                level = 0
            else:
                level += 1
        # 文字列を反転
        S = S[::-1]

    return ans if ans else "-1"

# 入力例
N = int(input())
S = input()
print(find_max_dango_level(S))

