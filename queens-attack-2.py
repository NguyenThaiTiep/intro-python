import abc


def QueensAtack(n, k, r_q, c_q, enemies_pos:list[list[int]]):
    x_q, y_q = r_q , c_q ;
    x = x_q

    atack_1 = [[1 if x_q + y_q <= n else (x_q + y_q - n),x_q + y_q - 1 if x_q + y_q <= n else n],[x_q + y_q - 1 if x_q + y_q <= n else n, 1 if x_q + y_q <= n else x_q + y_q - n]]
    atack_2 = [[x_q - y_q + 1 if x_q >= y_q else  1, 1 if x_q >= y_q else y_q -x_q + 1 ],[n if x_q >= y_q else n - y_q + x_q , n - x_q + y_q if x_q >= y_q else n ]]
    atack_3 = [[x_q,1],[x_q,n]]
    atack_4 = [[1,y_q],[n,y_q]]
    print( atack_1,atack_2, atack_3, atack_4)
    for [x,y] in enemies_pos:

        if x + y == x_q + y_q :
            #  nằm trên đường chéo từ trái -> phải, đi lên
            if x < x_q :
                x_a,y_a = atack_1[0]
                if x > x_a :
                    atack_1[0] = [x + 1,y - 1]
            else : 
                x_a,y_a = atack_1[1]
                if x < x_a:
                    atack_1[1] = [x - 1,y + 1]
        elif x - y == x_q - y_q :
            #  nằm trên đường chéo từ trái -> phải, đi xuống
            if x < x_q :
                x_a,y_a = atack_2[0]
                if  x > x_a :
                    atack_2[0] = [x + 1,y + 1]
            else : 
                x_a,y_a = atack_2[1]
                if x < x_a  :
                    atack_2[1] = [x - 1, y - 1]
        elif x == x_q :
            # cùng nằm trên trục song song y
            if y < y_q :
                x_a,y_a = atack_3[0]
                if  y > y_a :
                    atack_3[0] = [x ,y + 1]
            else : 
                x_a,y_a = atack_3[1]
                if y < y_a  :
                    atack_3[1] = [x,y - 1]
            pass
        elif y == y_q :
            # cùng nằm trên trục song song y
            if x < x_q :
                x_a,y_a = atack_4[0]
                if  x > x_a :
                    atack_4[0] = [x + 1,y]
            else : 
                x_a,y_a = atack_4[1]
                if x < x_a  :
                    atack_4[1] = [x - 1,y]
            
            pass
        pass
    result = 0
    for attack in [atack_1,atack_2, atack_3, atack_4]:
        start,end = attack
        x_1,y_1 = start;
        x_2,y_2 = end;
        if(x_1 == x_2 and y_1 == y_2) :
            continue
        result += abs(x_1 - x_2)  if x_1 != x_2 else abs(y_1 - y_2) 
        pass
    print( atack_1,atack_2, atack_3, atack_4)
    return result

r = QueensAtack(100,100,48 , 81,[[54, 87], [64, 97], [42, 75], [32, 65], [42, 87], [32, 97], [54, 75], [64, 65], [48, 87], [48, 75], [54, 81], [42, 81], [45, 17], [14, 24], [35, 15], [95, 64], [63, 87], [25, 72], [71, 38], [96, 97], [16, 30], [60, 34], [31, 67], [26, 82], [20, 93], [81, 38], [51, 94], [75, 41], [79, 84], [79, 65], [76, 80], [52, 87], [81, 54], [89, 52], [20, 31], [10, 41], [32, 73], [83, 98], [87, 61], [82, 52], [80, 64], [82, 46], [49, 21], [73, 86], [37, 70], [43, 12], [94, 28], [10, 93], [52, 25], [50, 61], [52, 68], [52, 23], [60, 91], [79, 17], [93, 82], [12, 18], [75, 64], [69, 69], [94, 74], [61, 61], [46, 57], [67, 45], [96, 64], [83, 89], [58, 87], [76, 53], [79, 21], [94, 70], [16, 10], [50, 82], [92, 20], [40, 51], [49, 28], [51, 82], [35, 16], [15, 86], [78, 89], [41, 98], [70, 46], [79, 79], [24, 40], [91, 13], [59, 73], [35, 32], [40, 31], [14, 31], [71, 35], [96, 18], [27, 39], [28, 38], [41, 36], [31, 63], [52, 48], [81, 25], [49, 90], [32, 65], [25, 45], [63, 94], [89, 50], [43, 41]])
print(r)