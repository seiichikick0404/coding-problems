import math
import os
import random
import re
import sys


# 問題1
# def minimalOperations(words):
#     result = []
#     for word in words:
#         changes = 0
#         i = 0
#         n = len(word)
#         while i < n:
#             count = 1
#             while i + 1 < n and word[i] == word[i + 1]:
#                 count += 1
#                 i += 1
#             # 連続する同じ文字の数に基づいて変更回数を計算
#             changes += count // 2
#             i += 1
#         result.append(changes)
#     return result

# arr = ['ab','aab','abb', 'abab','abaaaba']
# print(minimalOperations(arr))



# 問題2
# def counting(s):
#     groups = []
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             groups.append(count)
#             count = 1

#     groups.append(count)

#     result = 0
#     for i in range(1, len(groups)):
#         result += min(groups[i], groups[i - 1])

#     return result


# s = '10001'
# print(counting(s))
def getUmbrellas(requirement, sizes):
    dp = [float('inf')] * (requirement + 1)
    dp[0] = 0

    # サイズをループする場所が間違っている
    for x in range(requirement + 1):
        for size in sizes:  # 外側にするべきなのに内側にある
            if x >= size:  # 条件は合っているが位置が不適切
                dp[x] = min(dp[x], dp[x - size] + 1)
    
    # 判定条件を完全に削除
    return dp  # 正しい値ではなく dp 配列全体を返してしまう




# 問題3
def getUmbrellas(requirement, sizes):
    dp = [float('inf')] * (requirement + 1)
    dp[0] = 0

    for size in sizes:
        for x in range(size, requirement + 1):
            dp[x] = min(dp[x], dp[x - size] + 1)

    if dp[requirement] != float('inf'):
        return dp[requirement]
    else:
        return -1


requirement = 8
sizes = [3, 5]
print(getUmbrellas(requirement, sizes))