n=int(input("Nhập số năm:"))
von= 100
for nam_hien_tai in range (1,n+1 ):
    tong_tien= von + ((von*7)/100)
    von= tong_tien
    print(f"Tổng tiền trong {nam_hien_tai} năm là: {tong_tien}")