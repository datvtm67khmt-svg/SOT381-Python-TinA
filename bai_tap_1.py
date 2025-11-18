def kiem_tra_so(n):
    
    if (n % 2 == 0) and (n > 10) and (n % 3 == 0):
        print(f"Số {n} thỏa mãn đồng thời 3 điều kiện.")
        return True
    else:
        print(f"Số {n} KHÔNG thỏa mãn đồng thời 3 điều kiện.")
        return False

kiem_tra_so(29)
kiem_tra_so(20)
kiem_tra_so(999)