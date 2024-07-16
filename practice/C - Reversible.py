N = int(input())

sticks = [input() for _ in range(N)]
set_sticks = set(sticks)

unique_sticks = set()
for stick in sticks:
    reversed_stick = stick[::-1]
    unique_sticks.add(tuple(sorted([stick, reversed_stick])))

print(len(unique_sticks))
