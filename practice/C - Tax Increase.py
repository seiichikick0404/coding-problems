import math

A, B = map(int, input().split())

# Initialize a flag to check if a valid price is found
found = False

# Increase the search range if necessary
for i in range(1, 2000):  # Adjust the upper limit based on the problem's constraints
    A_price = math.floor(i * 0.08)
    B_price = math.floor(i * 0.1)

    if A == A_price and B == B_price:
        print(i)  # Print the first matching price
        found = True  # Set the flag to True indicating a match is found
        break  # Exit the loop after finding the first match

if not found:
    print(-1)  # If no matching price is found, print -1

# Notes:
# The script searches for the smallest integer price within the range 1 to 1999
# that satisfies the condition where the tax at 8% is A, and the tax at 10% is B.
# The range is chosen arbitrarily and should be adjusted according to


