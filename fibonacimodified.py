def fibonaciModified(t1:int, t2:int, n:int):
    if n == 1 : return t1
    if n == 2 : return t2
    
    # t(i + 2) = t(i)  + t(i+1) ^2
    return fibonaciModified(t1,t2,n - 2) + pow(fibonaciModified(t1,t2, n -1), 2)
a = fibonaciModified(0,1,6)
print(a)