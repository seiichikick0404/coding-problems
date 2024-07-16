def generate_parentheses(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)

    ans = []
    backtrack()
    return ans

N = int(input())
if N % 2 != 0:
    print()
    exit()

correct_parentheses = generate_parentheses(N // 2)  # Nはカッコのペアの数なので半分にする
print(correct_parentheses)
for cp in correct_parentheses:
    print(cp)
