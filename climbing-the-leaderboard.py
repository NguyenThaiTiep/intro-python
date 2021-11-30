def indexItem(arr : list[int], value:int):
    index = 0
    while index < len(arr):
        print(index)
        if value >= arr[index] :
            
            return index + 1
        
    return len(arr)
    
def Ranking(ranks : list[int], scores : list[int]):
        rankD = list(set(ranks))
        rankD.sort()
        rankD.reverse()
        myRanks = [len(rankD) + 1 for _ in scores]
        for i,score in enumerate(scores) :
            myRanks[i] = indexItem(rankD, score)
        print(myRanks)
        return myRanks
Ranking([100,100,50,40,40,20,10], [5,25,50,120])

# [100, 50, 40, 20, 10]
# [5,25,50,120]