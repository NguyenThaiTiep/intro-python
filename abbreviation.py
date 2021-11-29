# cho 2 chuỗi kĩ tự a và b (toàn kí tự in hoa)
# có thế biến đổi a bằng 1 trong 2 cách sau
# - chuyển 0 hoặc nhiều kí tự thường thành kí tự viết hoa
# - xoá  tẩt các các kí tự thường (chỉ để lại kí tự viết hoa)
# Hỏi có thể có hữu hạn bước để chuyển từ a  -> b hay không
# nếu có return true
def abbreviation(a:str,b:str):
    # retur false khi 
    """
    - tạo 1 mảng 2 chiều có kích thước là mxn X(m, n) là độ dài của các chuỗi kí tự a,b
    - i,j lần lượt là số thứ tự của a,b
    - giá trị khởi tạo của mảng 2 chiều lần lượt là -1  (nếu i < j), và 0 (các th còn lại)
    - tại giá trị [i,j] có 3 trường hợp xảy ra
     1. nếu a[i] = b[j] thì không biến đổi
     2. nếu a[i] là chữ thường thì có thể biến đổi (xoá hoặc chuyển thành chữ hoa)
     3. nếu a[i] là chữ hoa và khác b[j] thì không thế biến đổi, X[i,j] = -1
    """ 
    lenA,lenB = len(a), len(b)
    X = [[i for i in range(lenB)] for j in range(lenA)]

    for i,u in enumerate(X) : 
        for j, v in enumerate(u) :
            if i < j : 
                X[i][j] = -1
                continue;
            
            # th1 : a[i] = b[i]
            if a[i] == b[j] :
                if i == 0 and j == 0:
                    X[i][j] = 0
                elif j == 0:
                    X[i][j] = X[i -1][j]
                else:
                     X[i][j] =  X[i - 1][j -1]
            elif a[i].islower():
                if a[i].upper() == b[j]:
                    if i == j :
                        X[i][j] = 1 if j == 0 else -1 if  X[i - 1][j - 1]== -1 else X[i - 1][j - 1] + 1
                    else:
                        if X[i - 1][j] != -1 : X[i][j] = X[i -1][j] +1
                        elif X[i - 1][j - 1] != -1 : X[i][j] = X[i - 1][j -1] + 1
                        else:
                            X[i][j] = -1
                            
                else:
                    if i == j :
                        X[i][j] = -1 if j != 0 else 1  
                    else:
                        X[i][j] = X[i - 1][j] + 1  if  X[i - 1][j] != -1 else -1
                    
                    
            else:
                #  là chữ hoa
                X[i][j] = -1;
                
    print(X)       
    return X[lenA-1][lenB - 1] != -1
result = abbreviation(
    'rararaarraraaraArarrrraaaqararraararrrrrrraarrrrarAarraaaarraaryrraaarrraararrardaaarrrRaaarrRraaRarrrrrarraraaaaarrrarrararraarrararrrraraaaaarrarrrrraaarrrrarrrarararraraaaaaarrrararrrraRaraAraaraARARaraarraarararaarrarrArAraAarrrrarrrrRrrraraaraaarrraraaarrrarrrraRarararrraraaraaarraaaaaAaaarrrararraaaaararRaaarraaaRrarraraaaaraaarrrarraarraaraaarrraaaaararrrwraraaaraarraaarrraaararaaarraraaaaarrrrarrrraaaarrarrrrrararararararrArarraaaaraAArrrarrrArrArrAraarRrraraaaAraaarrrarraarnraaaaarraaraaaaraaararaaarrarraarraararraaraAaraaaraaaaaaaaArrrrrarararaaraarRaarrrrraarrraraararaaararaarraAraaaaArrAraarArrararrraarrararrrarRarrrrrrarrrrarraarraarrarrraraaaaararAarararaarraaRararrArarAaraaarrrrraaaaarrrraararraaraaraauaraaaaraaarrrarrrrrraarroaraarrrrarraraRrrraaaaarrraarraarrrraararrrrhraarrarrraaaaarararRrarArrrraraaaarArraarraarraraaaraarrrAaaaraaraaaaraaararaArrrraaarrararrarrraararaarrrrrarArrarrrraaaraarrrraaRarrrrararaaararrrarrararaaarararraarRraaarRrrrrraraarrraraarraraarrRarar', 
    'RARARAARRARAAAARRRRRAAAARARRAARARRRRRRRAARRRRARAARRAAAARRAARRRAAARRRAARARRARAAARRRRAAARRRRAARARRRRRARRARAAAAARRRARRARARRAARRARARRRRARAAAAARRARRRRRAAARRRRARRRARARARRARAAAAAARRRARARRRRARARAARAARAARARARAARRAARARARAARARRARARAAARRRRARRRRRRRRARAARAARRRARAAARRRARRRRARARARARRRARAARAAARRAAAAAAAAARRRARARAAAAARARRAARRAAARRARRARAAAARAARRRARRAARRAARAAARRRAAAAARARRRRARAAARAARRAAARRRAARARAAARRARAAAAARRRRARRRRAAAARRARRRRRARARARARARARRARARRAAAARAAARRRARRRARRARRARAARRRRAAAAARAAARRRRRAAAAAAARRAARAAARAARARAAARRARRAARRAARARRAARAAAAAARAAAAAAAAARRRRRAARARAARAARRARRRRRAARRARAARRAAARARAARRAARAAAAARRARAARARARARRRAARRARARRRARRARRRRRRARRRRARRAARRAARRARRRARAAAAARARAARARAAARRAARARARRARARAARAAARRRRRAAAARRRAARARRAAAARAAARAAAARAAARRRARRRRRRAARRARAARRRRARRARARRRRAAAAARRRAARRAARRRAARARRRRRARARRRAAAAARARARRRARARRRRARAAARARAARAARRAAAARAARRRAAAARARAAAARAARARAARRRRAAARRARRRARRRARARAARRRRRARARRARRRAAARAARRRRAAARRRRARARAAARARRRARARRAAARARARRARRRAARRRRRRRARAARRARAARRARAARRRARAR')
print("YES" if result else "No")