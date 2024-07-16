def compare_powers(a, b, c):
    ac_minus = (c % 2 == 1) and (a < 0)
    bc_minus = (c % 2 == 1) and (b < 0)

    if ac_minus != bc_minus:
        if ac_minus:
            return "<"
        else:
            return ">"
    else:
        if abs(a) == abs(b):
            return "="
        elif (abs(a) < abs(b)) != ac_minus:
            return "<"
        else:
            return ">"

# 標準入力から値を受け取る部分は、以下のようになります
a, b, c = map(int, input().split())
print(compare_powers(a, b, c))