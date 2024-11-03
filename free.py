
total_odd = 0
total = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            i_str = str(i)
            j_str = str(j)
            k_str = str(k)
            ans = int(i_str + j_str + k_str)
            if ans % 2 != 0:
                total_odd += 1

            if ans > 230:
                total += 1



print(total_odd)
print(total)


