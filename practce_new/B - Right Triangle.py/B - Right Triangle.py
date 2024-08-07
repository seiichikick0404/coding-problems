A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 各辺の長さを調べる
def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

AB2 = distance(A, B)
AC2 = distance(A, C)
BC2 = distance(B, C)


# 三平方の定理を使って直角三角形かどうかを判定する
def is_right_triangle(a2, b2, c2):
    return a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2

# 直角三角形の判定
if is_right_triangle(AB2, AC2, BC2):
    print('Yes')
else:
    print('No')


