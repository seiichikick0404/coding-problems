n = int(input())

nums = list(map(int, input().split()))

l_200 = [0] *  200

for num in nums:
    remainder = num % 200
    l_200[remainder] += 1

# 各余りから作れるペアの数を計算
total_pairs = 0
for count in l_200:
    if count > 1:
        total_pairs += count * (count - 1) // 2

print(total_pairs)