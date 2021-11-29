def staircase(n):
    # Write your code here
    for i in range(n):
        print(" "*(n - 1 - i), end="")
        print("#"*(i +1 ))
print(staircase(2))