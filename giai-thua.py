def extraLongFactorials(n):
    # Write your code here
    if n == 1 : return 1
    return extraLongFactorials(n - 1) * n
print(extraLongFactorials(25))