def chuyen_doi_nhiet_do():
    print("=== CHƯƠNG TRÌNH CHUYỂN ĐỔI NHIỆT ĐỘ ===")
    
    try:
        nhiet_do_dau = float(input("Nhập giá trị nhiệt độ: "))
        loai_dau = input("Nhập loại nhiệt độ gốc (C, F, hoặc K): ").upper()
    except ValueError:
        print("Lỗi: Giá trị nhiệt độ phải là một số.")
        return
        
    if loai_dau not in ['C', 'F', 'K']:
        print("Lỗi: Loại nhiệt độ không hợp lệ. Vui lòng nhập C, F, hoặc K.")
        return

    print("\n--- KẾT QUẢ CHUYỂN ĐỔI ---")
    
    C = None 
    F = None
    K = None

    # 1. Chuyển về Celsius (C) làm gốc
    if loai_dau == 'C':
        C = nhiet_do_dau
    elif loai_dau == 'F':
        C = (nhiet_do_dau - 32) * (5/9)
    elif loai_dau == 'K':
        C = nhiet_do_dau - 273.15

    # 2. Từ C, tính ra F và K
    if C is not None:
        if loai_dau != 'F':
            F = C * (9/5) + 32
        else:
            F = nhiet_do_dau
            
        if loai_dau != 'K':
            K = C + 273.15
        else:
            K = nhiet_do_dau

    # 3. PHẦN BỔ SUNG: IN KẾT QUẢ RA MÀN HÌNH
    print(f"Nhiệt độ gốc: {nhiet_do_dau:.2f} {loai_dau}")
    print("-" * 30)

    if loai_dau != 'C':
        print(f"Chuyển sang Celsius (C): {C:.2f} °C")
    if loai_dau != 'F':
        print(f"Chuyển sang Fahrenheit (F): {F:.2f} °F")
    if loai_dau != 'K':
        print(f"Chuyển sang Kelvin (K): {K:.2f} K")
    print("-" * 30)
chuyen_doi_nhiet_do()