def dien_tich_hinh_thang():
    try:
        day_lon = float(input("Nhập độ dài đáy lớn (a): "))
        day_be = float(input("Nhập độ dài đáy bé (b): "))
        chieu_cao = float(input("Nhập chiều cao (h): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ.")
        return

    if day_lon <= 0 or day_be <= 0 or chieu_cao <= 0:
        print("Lỗi: Độ dài các cạnh và chiều cao phải là số dương.")
        return

    dien_tich = (day_lon + day_be) * chieu_cao / 2

    print("-" * 30)
    print(f"Đáy lớn (a) = {day_lon}, Đáy bé (b) = {day_be}, Chiều cao (h) = {chieu_cao}")
    print(f"Diện tích hình thang là: {dien_tich:.2f}")
    print("-" * 30)

dien_tich_hinh_thang()