def shift_border(matrix):
    n = len(matrix)
    ans = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j < n - 1:
                ans[i][j + 1] = matrix[i][j]
            elif i < n - 1 and j == n - 1:
                ans[i + 1][j] = matrix[i][j]
            elif i == n - 1 and j > 0:
                ans[i][j - 1] = matrix[i][j]
            elif i > 0 and j == 0:
                ans[i - 1][j] = matrix[i][j]
            else:
                ans[i][j] = matrix[i][j]
    return ans

def main():
    n = int(input().strip())
    matrix = []
    for _ in range(n):
        s = input().strip()
        matrix.append([int(ch) for ch in s])
    
    ans = shift_border(matrix)
    
    for row in ans:
        print(''.join(str(num) for num in row))

if __name__ == "__main__":
    main()
