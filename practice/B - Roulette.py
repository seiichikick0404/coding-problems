



# {
#     1: 3,
#     2: 4,
#     4: 3
# }



# Nを取得
N = int(input())

# 各人が賭ける目の情報を保存するリスト
bets = []

# N回ループを回す
for _ in range(N):
    # Ciを取得
    Ci = int(input())
    # Ci個の目の情報を取得して、リストとして保存
    Ai = list(map(int, input().split()))
    # betsに追加
    bets.append(Ai)

# Xを取得
X = int(input())

ans = {}
for i in range(N):
    if X in bets[i]:
        ans[i+1] = len(bets[i])

if not ans:
    print(0)
    exit()

# 最小の賭けた数を見つける
min_bets = min(ans.values())

# # 最小の賭けた数に一致するすべてのキー（人の番号）を取得
min_bettors = [person for person, bet in ans.items() if bet == min_bets]

print(len(min_bettors))
print(*min_bettors)



