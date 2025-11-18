def thap_phan_sang_nhi_phan():
    try:
        thap_phan = int(input("Nhập một số nguyên dương: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên dương hợp lệ.")
        return

    if thap_phan < 0:
        print("Lỗi: Vui lòng nhập số nguyên dương.")
        return
    
    if thap_phan == 0:
        nhi_phan = "0"
    else:
        nhi_phan = bin(thap_phan)[2:] 

    print("-" * 40)
    print(f"Số thập phân: {thap_phan}")
    print(f"Dạng nhị phân là: {nhi_phan}")
    print("-" * 40)

thap_phan_sang_nhi_phan()