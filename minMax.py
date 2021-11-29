# Given five positive integers, 
# find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
#  Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def maxMinSum(arr:list[int]) : 
    n = len(arr)
    sums = [x for x in arr]
    sums.sort()
    maximum = sum(sums[0:4])
    minimum = sum(sums[n - 4: n ])
    print(f'{maximum} {minimum}')
arr = [7,69,2,221,8974]
maxMinSum(arr)