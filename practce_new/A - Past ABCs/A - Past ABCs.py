S = input()
digits = int(S[-3:])

range1 = range(1, 316)
range2 = range(317, 350)

if digits in range1 or digits in range2:
    print('Yes')
else:
    print('No')


