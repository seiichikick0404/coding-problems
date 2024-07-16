N, M = map(int, input().split())

S = list(input().split())
T = list( input().split())

express_stations = set(T)

for station in S:
    if station in express_stations:
        print('Yes')
    else:
        print('No')
    