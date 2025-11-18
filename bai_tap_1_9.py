def doi_so_tien_thanh_menh_gia():
    menh_gia = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    
    try:
        so_tien = int(input("Nhập số tiền cần đổi (VND): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số tiền nguyên hợp lệ.")
        return

    if so_tien <= 0:
        print("Lỗi: Số tiền phải là số dương.")
        return

    print("\n--- SỐ LƯỢNG CÁC MỆNH GIÁ CẦN THIẾT ---")
    
    tien_con_lai = so_tien
    
    for mg in menh_gia:
        so_luong = tien_con_lai // mg
        if so_luong > 0:
            print(f"{mg:,} VND: {so_luong} tờ/đồng")
            tien_con_lai %= mg

    if tien_con_lai > 0:
        print(f"Số tiền còn lại không đổi được: {tien_con_lai:,} VND")
        
    print("-" * 40)

doi_so_tien_thanh_menh_gia()