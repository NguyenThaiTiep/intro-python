# in ra các số từ 2 - 10 và kiểm tra số đó có phải là nguyên tố không 
for x in range(2, 10) : 
    for d in range(2,x) : 
        if(x % d == 0):
            print(f"Số {x} không phải là số nguyên tố")
            break;
    else : 
        print(f"Số {x} là số nguyên tố")
