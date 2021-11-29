def diagonalDifference(arr :list[list[int]]):
    # Write your code here
    arrLeft = [num for i,element in enumerate(arr) for index,num in enumerate(element) if i == index]
    arrRight = [num for i,element in enumerate(arr) for index,num in enumerate(element) if len(arr) - i - 1 == index]
    print(sum(arrRight))
    
    return arrLeft;
arr = [[1,2,3], [4,5,6], [9,8,8]]
print(diagonalDifference(arr))