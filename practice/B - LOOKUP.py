
S = input()
T = input()

found = False
for i in range(len(S) - len(T) + 1):
    if S[i:i+len(T)] == T:
        found = True
        break

if found:
    print("Yes")
else:
    print("No")
