# xác định số chẵn - lẻ tử 1 - 10
for x in range(1,10):
    if not x % 2:
        print(f"{x} là số chẵn")
        continue 
    print(f"{x} là số lẻ")
