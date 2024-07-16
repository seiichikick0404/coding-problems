def check(ans):
    curr = 0
    for s in ans:
        if s == "A":
            curr += 1
        else:
            curr *= 2

    return curr


N = int(input())

ans = ""
while N > 1:
    if N % 2 == 0:
        ans = "B" + ans
        N //= 2
    else:
        ans = "A" + ans
        N -= 1

# 最後の1は常にAの操作で達成できる
ans = "A" + ans


print(ans)


