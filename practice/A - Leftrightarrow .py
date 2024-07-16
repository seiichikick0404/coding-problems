S = input()

left_right = False
center = False
if S[0] == "<" and S[-1] == ">":
    left_right = True


for s in S[1:-1]:
    if s != "=":
        print('No')
        exit()

center = True


if left_right and center:
    print('Yes')
else:
    print('No')