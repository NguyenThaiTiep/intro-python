def NonDivisible( arr:list[int], k):
    modArr = [ 0 for x in range(0, k)]
    if k == 1: return 1
    for x in arr : 
        modArr[x % k] += 1
    a = 0
    # print(modArr)
    print(modArr)
    for x in range(1,k//2 + 1) :
        if x == k / 2 and  k % 2 == 0: 
            continue
        a +=  max(modArr[x], modArr[k - x])
    # sau khi đã có mảng gồm cac phần tử không bao gồm K // 2
    # nếu k chia hết cho 2, thì thêm 1 số có số dư = k/ 2 thì đểu thoả mãn
        if k % 2 == 0 : 
            a+= 1
        if(modArr[0]) : 
            a += 1
    return a

    
print(NonDivisible([1,2,3,4,5, 6,7, 8 , 9 ,10],4))