N = int(input())
name_rate_list = []
total = 0

for i in range(N):
    name, rate = input().split()
    name_rate_list.append((name, int(rate)))
    total += int(rate)

sorted_data = sorted(name_rate_list, key=lambda x: x[0])

index = total % N

print(sorted_data[index][0])




