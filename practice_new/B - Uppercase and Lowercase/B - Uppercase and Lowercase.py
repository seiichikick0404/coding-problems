
S = input()

low_count = 0
for s in S:
    if s.islower():
        low_count += 1


if len(S) // 2 < low_count:
    print(S.lower())
else:
    print(S.upper())
