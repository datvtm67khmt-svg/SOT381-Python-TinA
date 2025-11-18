def chuyen_doi_giay():
    try:
        tong_giay = int(input("Nhập tổng số giây cần chuyển đổi: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
        return

    if tong_giay < 0:
        print("Lỗi: Số giây không thể là số âm.")
        return

    gio = tong_giay // 3600
    phut = (tong_giay % 3600) // 60
    giay = tong_giay % 60

    print("-" * 50)
    print(f"{tong_giay} giây tương đương với:")
    print(f"{gio} giờ, {phut} phút, {giay} giây.")
    print(f"Định dạng HH:MM:SS là: {gio:02d}:{phut:02d}:{giay:02d}")
    print("-" * 50)

chuyen_doi_giay()