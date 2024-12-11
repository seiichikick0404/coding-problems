S = input()

result_set = set()
for s in S:
    if s == "A" or s == "B" or s == "C":
        result_set.add(s)

if len(result_set) == 3:
    print('Yes')
else:
    print('No')
