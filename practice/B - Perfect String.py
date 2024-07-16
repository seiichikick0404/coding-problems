S = input()
original_count =  len(S)

S_set = set(list(S))
set_count = len(S_set)

# 相違チェック
if original_count != set_count:
    print('No')
    exit()


lower = False
upper = False
# 小文字or大文字チェック
for s in S:
    if s.islower():
        lower = True

    if s.isupper():
        upper =  True

if lower and upper:
    print('Yes')
else:
    print('No')