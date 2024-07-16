N, K = map(int, input().split())
l = list(map(int, input().split()))

bottom, top = 0, 10 ** 10

def cnt(t):
    ans = 0
    for a in l:
        ans += t // a
    return ans


while top - bottom > 1:
    mid = bottom + (top - bottom) // 2
    if (cnt(mid) < K):
        bottom = mid
    else:
        top = mid

print(top)