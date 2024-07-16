X = int(input())

dp = [False] * (X + 6)
dp[0] = True

print(dp)

for x in range(0, X):
    if dp[x]:
        for d in range(6):
            if x + 100 + d <= X:
                dp[x + 100 + d] = True
print(dp)
if dp[X]:
    print(1)
else:
    print(0)





# def solve(X):
#     dp = [False] * (X + 6)  # X+5まで確認する必要があるため、配列サイズをX+6に設定
#     dp[0] = True  # 0円は常に構成可能

#     # dpテーブルを更新
#     for x in range(0, X):
#         if dp[x]:
#             for d in range(6):  # 100円から105円まで
#                 if x + d + 100 <= X:  # 配列の範囲を超えないようにチェック
#                     dp[x + d + 100] = True

#     # 最終的な判断
#     if dp[X]:
#         return 1
#     else:
#         return 0

# # 例として615をテスト
# X = int(input())
# print(solve(X))

