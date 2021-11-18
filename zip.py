matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# arry 3x4 to 4x3
array = list(zip(*matrix))
print(array)