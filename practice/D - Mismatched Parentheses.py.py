N = int(input())
S = input()

stack = []
cnt = 0
for i in range(N):
    s = S[i]
    if s == '(':
        cnt += 1

    if cnt > 0 and s == ')':
        while True:
            cur = stack.pop()
            if cur == '(':
                break
        cnt -= 1
        continue

    stack.append(s)

print(''.join(stack))