N = int(input())
A = list(map(int, input().split()))

ans = [0]
curr_angle = 0

for i in range(N):
    curr_angle = (curr_angle + A[i]) % 360

    # 切れ目が入っていない場合追加
    if curr_angle not in ans:
        ans.append(curr_angle)


ans.sort()
ans.append(360)  # 360度を追加して円を閉じる

max_angle = 0
for i in range(len(ans) -1):
    diff_angle = ans[i+1] - ans[i]
    max_angle = max(max_angle, diff_angle)

print(max_angle)
