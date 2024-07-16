

def is_over_price(A, B):
    return A >= B




def is_upper_compatible(products):
    for i in range(len(products)):
        for j in range(len(products)):
            # 同じ商品を比較しない
            if i == j:
                continue
            
            price_i, features_i = products[i][0], products[i][1:]
            price_j, features_j = products[j][0], products[j][1:]
            
            # 条件1: 商品iの価格が商品jの価格以上
            if price_i < price_j:
                continue
            
            # 条件2: 商品jのすべての機能が商品iに含まれているか
            if not all(feature in features_i for feature in features_j):
                continue
            
            # 条件3: 商品iの価格が商品jより高いか、商品iに商品jにない機能がある
            if price_i > price_j or any(feature not in features_j for feature in features_i):
                return "Yes"
    
    return "No"

N, M = map(int, input().split())
products = [list(map(int, input().split())) for i in range(N)]

print(is_upper_compatible(products))


