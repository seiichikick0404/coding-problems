import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    left_index = 0
    right_index = len(arr) -1
    left_total = 0
    right_total = 0
    for i in range(len(arr)):
        row = arr[i]
        left_total += row[left_index]
        right_total += row[right_index]
        left_index += 1
        right_index -= 1

    return abs(left_total - right_total)

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
result = diagonalDifference(arr)
print(result)
