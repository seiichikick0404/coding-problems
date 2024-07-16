N, M = map(int, input().split())

players = [i for i in range(1, N+1)]
for i in range(M):
    win,lose = map(int,input().split())
    if lose in players:
        players.remove(lose)

    

if len(players) > 1:
    print(-1)
else:
    print(players[0])

