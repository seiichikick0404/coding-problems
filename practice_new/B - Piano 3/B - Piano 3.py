N = int(input())

left_hands = []
right_hands = []

for _ in range(N):
    val, hand = input().split()
    if hand == "L":
        left_hands.append(int(val))
    else:
        right_hands.append(int(val))


total = 0
for i in range(1, len(left_hands)):
    total += abs(left_hands[i] - left_hands[i-1])


for i in range(1, len(right_hands)):
    total += abs(right_hands[i] - right_hands[i-1])

print(total)