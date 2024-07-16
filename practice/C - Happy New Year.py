


        


K = int(input())

for i in range(1, 10000000 + 1):
    # Check if the number consists of only 0s and 2s
    count = 0
    if all(char in ['0', '2'] for char in str(i)):
        if count == K:
            print(i)
            exit()
        
        count += 1