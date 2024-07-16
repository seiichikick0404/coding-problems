
ABC = False
ARC = False
AGC = False
AHC = False

for i in range(3):
    S = input()
    if S == "ABC":
        ABC = True
    elif S == "ARC":
        ARC = True
    elif S == "AGC":
        AGC = True
    elif S == "AHC":
        AHC = True

if not ABC:
    print("ABC")
elif not ARC:
    print('ARC')
elif not AGC:
    print('AGC')
else:
    print('AHC')


