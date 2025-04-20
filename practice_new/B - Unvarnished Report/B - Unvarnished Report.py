S = input()
T = input()

max_len = max(len(S), len(T))
for i in range(max_len):
    try:
        if S[i] != T[i]:
            print(i+1)
            exit()
    except IndexError:
        print(i+1)
        exit()

print(0)