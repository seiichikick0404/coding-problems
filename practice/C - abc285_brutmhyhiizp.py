S = input()


hash_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
 }

def calculate_position_improved(s, hash_map):
    length = len(s)
    total = 0

    # Adding the number of strings for all lengths smaller than the current length
    for i in range(1, length):
        total += 26 ** i

    # Calculating the position of the given string using the hash_map
    for i, char in enumerate(s):
        total += (hash_map[char] - 1) * (26 ** (length - i - 1))

    return total + 1  # Adding 1 because 'A' is the first position, not zero


print(calculate_position_improved(S, hash_map))




