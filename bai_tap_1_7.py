def chu_vi_dien_tich_hcn():
    try:
        dai = float(input("Nhập chiều dài hình chữ nhật: "))
        rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ.")
        return

    if dai <= 0 or rong <= 0:
        print("Lỗi: Chiều dài và chiều rộng phải là số dương.")
        return

    chu_vi = 2 * (dai + rong)
    dien_tich = dai * rong

    print("-" * 40)
    print(f"Chiều dài = {dai}, Chiều rộng = {rong}")
    print(f"Chu vi hình chữ nhật là: {chu_vi:.2f}")
    print(f"Diện tích hình chữ nhật là: {dien_tich:.2f}")
    print("-" * 40)

chu_vi_dien_tich_hcn()