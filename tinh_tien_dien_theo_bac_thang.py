def tinh_tien_dien_theo_bac_thang():
    print("=== CHƯƠNG TRÌNH TÍNH TIỀN ĐIỆN THEO BẬC THANG ===")
    
    try:
        so_dien = int(input("Nhập số kWh tiêu thụ (số nguyên): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
        return

    if so_dien < 0:
        print("Lỗi: Số kWh tiêu thụ không thể là số âm.")
        return

    tong_tien = 0
    con_lai = so_dien
    
    bac_thang = [
        (50, 1678),    
        (50, 1734),    
        (100, 2014),   
        (150, 2536),   
        (float('inf'), 2927) 
    ]

    print("\n--- CHI TIẾT TÍNH TOÁN ---")

    for gioi_han, gia in bac_thang:
        if con_lai > 0:
            so_su_dung = min(con_lai, gioi_han)
            tien_bac = so_su_dung * gia
            tong_tien += tien_bac
            con_lai -= so_su_dung
            
            if gioi_han != float('inf'):
                print(f"Bậc {bac_thang.index((gioi_han, gia)) + 1}: {so_su_dung:<5} kWh * {gia:>5} VND/số = {tien_bac:>10,.0f} VND")
            else:
                 print(f"Bậc cuối: {so_su_dung:<5} kWh * {gia:>5} VND/số = {tien_bac:>5} VND = {tien_bac:>10,.0f} VND")
    
    print("-" * 40)
    print(f"Tổng số kWh tiêu thụ: {so_dien:,.0f} kWh")
    print(f" TỔNG TIỀN ĐIỆN CẦN THANH TOÁN: {tong_tien:,.0f} VND")
    print("-" * 40)

tinh_tien_dien_theo_bac_thang()