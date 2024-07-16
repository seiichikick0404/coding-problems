S = input()

columns = [
    S[6],
    S[3] + S[7],
    S[1] + S[4] + S[8],
    S[0] + S[2] + S[5] + S[9],
]

# Check if pin 1 is down
if columns[3][0] == "0":
    print('Yes')
else:
    # Store indices of columns with standing pins
    standing_pin_columns = [i for i, col in enumerate(columns) if "1" in col]

    # Check if there's a column with all pins down between columns with standing pins
    is_split = False
    for i in range(len(standing_pin_columns) - 1):
        if standing_pin_columns[i+1] - standing_pin_columns[i] > 1:
            is_split = True
            break
    
    print('Yes' if is_split else 'No')




