import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_min_prime(X):
    while True:
        if is_prime(X):
            return X
        X += 1

# Xの値を入力
X = int(input())

# 結果の出力
print(find_min_prime(X))
