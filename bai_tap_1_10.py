def trung_binh_cong():
    try:
        a = float(input("Nhập số thứ nhất (a): "))
        b = float(input("Nhập số thứ hai (b): "))
        c = float(input("Nhập số thứ ba (c): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập các số thực hợp lệ.")
        return

    trung_binh = (a + b + c) / 3

    print("-" * 30)
    print(f"Ba số đã nhập: {a}, {b}, {c}")
    print(f"Giá trị trung bình cộng là: {trung_binh:.3f}")
    print("-" * 30)

trung_binh_cong()