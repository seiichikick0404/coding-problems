Y = int(input())

if not Y % 4 == 0:
    print(365)
elif Y % 4 == 0 and not Y % 100 == 0:
    print(366)
elif Y % 100 == 0 and not Y % 400 == 0:
    print(365)
else:
    print(366)