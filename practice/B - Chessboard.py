
grid =  [input() for _ in range(8)]

col_map = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

row_map = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}



for i in range(8):
    for j in range(8):
        if grid[i][j] == "*":
            print(col_map[j] + row_map[i])
            exit()
