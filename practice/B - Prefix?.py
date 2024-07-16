s = input()
t = input()

t_pre = t[:len(s)]

if s == t_pre:
    print('Yes')
else:
    print('No')