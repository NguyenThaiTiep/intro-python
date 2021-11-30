def coinChange(S,numbers :list[int]):
    n = len(numbers)
    L = [[1 if i ==0 else 0 for x in range(0,n)] for i in range(0,S +1)]
    for i in range(1, S + 1) :
        for j in range(0, n) :
            # L[i,j] = sum(L[i - k * numbers[j]][j - 1]), k : 0 -> i/number[j]
            if j == 0 :
                L[i][j] =1 if i % numbers[j] == 0 else 0 
                continue
            sum = 0
            maxIndex = int(i/numbers[j])
            # print(maxIndex)
            for k in range(0, maxIndex+1):
                sum += L[i - k *numbers[j]][j - 1] if j >= 1 else 0
            L[i][j] = sum
    return L[S][n - 1]
print(coinChange(4, [1,2,3]))
