def extraLongFactorials(n):
    # Write your code here
    ans = n
    for i in range(1, n):
        ans = ans * (n - i)

    return ans 


result = extraLongFactorials(25)
print(result)