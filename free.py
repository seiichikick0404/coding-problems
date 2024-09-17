S = input()
N = int(input())

menus = input().split()
for menu in menus:
    if menu == S:
        print("Yes")
        exit()

print("No")
