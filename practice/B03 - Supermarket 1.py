# N = 商品数
# Ai 商品の金額

N = int(input())
priceList = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (priceList[i] + priceList[j] + priceList[k] == 1000):
                print("Yes")
                exit()



print("No")

